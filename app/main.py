# MIT License

# Copyright (c) 2026 Victor

# This file is part of the Class_one_victor_ai project.
# See the LICENSE file in the project root for full license information.

# FastAPI entry point for Class_one_victor_ai

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.config import victor_get_config
from app.models import Victor_ChatRequest, Victor_ChatResponse
from app.openai_service import Victor_OpenAIService
from app.store import Victor_SessionStore


# Resolve project root directory
victor_project_root = Path(__file__).resolve().parent.parent

# Load configuration
victor_config = victor_get_config()

# Initialize FastAPI app
victor_app = FastAPI(title=victor_config.victor_app_title)

# Setup templates and services
victor_templates = Jinja2Templates(directory=str(victor_project_root / "templates"))
victor_openai_service = Victor_OpenAIService()
victor_session_store = Victor_SessionStore()

# Serve static files
victor_app.mount(
    "/static",
    StaticFiles(directory=str(victor_project_root / "static")),
    name="static",
)


@victor_app.get("/", response_class=HTMLResponse)
def victor_home_page(victor_request: Request) -> HTMLResponse:
    # Render the simple browser interface

    return victor_templates.TemplateResponse(
        "index.html",
        {"request": victor_request, "victor_title": victor_config.victor_app_title},
    )


@victor_app.get("/health")
def victor_health_check() -> dict[str, str]:
    # Return basic status to confirm the app is running

    return {"status": "running", "application": victor_config.victor_app_title}


@victor_app.post("/chat", response_model=Victor_ChatResponse)
def victor_chat(victor_request_body: Victor_ChatRequest) -> Victor_ChatResponse:
    # Handle one chat request and maintain conversation state using session id

    try:
        # Get previous response id for this session (if exists)
        victor_previous_response_id = victor_session_store.victor_get_previous_response_id(
            victor_request_body.victor_session_id
        )

        # Send message to OpenAI
        victor_response = victor_openai_service.victor_send_chat_message(
            victor_user_message=victor_request_body.victor_message,
            victor_previous_response_id=victor_previous_response_id,
        )

        # Save new response id for future requests
        victor_session_store.victor_set_previous_response_id(
            victor_session_id=victor_request_body.victor_session_id,
            victor_response_id=victor_response.id,
        )

        # Return response to client
        return Victor_ChatResponse(
            victor_session_id=victor_request_body.victor_session_id,
            victor_response_id=victor_response.id,
            victor_reply=victor_response.output_text,
        )

    except Exception as victor_error:
        # Return error as HTTP 500
        raise HTTPException(status_code=500, detail=str(victor_error)) from victor_error


@victor_app.delete("/chat/{victor_session_id}")
def victor_clear_chat(victor_session_id: str) -> dict[str, str]:
    # Clear stored conversation state for a session

    victor_session_store.victor_clear_session(victor_session_id)
    return {"status": "cleared", "victor_session_id": victor_session_id}