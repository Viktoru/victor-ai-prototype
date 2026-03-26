# MIT License

# Copyright (c) 2026 Victor

# This file is part of the Class_one_victor_ai project.
# See the LICENSE file in the project root for full license information.

# Pydantic models used by the API

from pydantic import BaseModel, Field


class Victor_ChatRequest(BaseModel):
    # Incoming request body for a chat message

    # Unique session identifier to track conversation state
    victor_session_id: str = Field(..., min_length=1, description="Client session identifier")

    # User message sent to the AI
    victor_message: str = Field(..., min_length=1, description="User message sent to the AI")


class Victor_ChatResponse(BaseModel):
    # Outgoing response returned by the API

    # Session identifier
    victor_session_id: str

    # OpenAI response id (used for conversation state)
    victor_response_id: str

    # AI-generated reply
    victor_reply: str