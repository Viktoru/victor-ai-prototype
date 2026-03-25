"""Pydantic models used by the API."""

from pydantic import BaseModel, Field


class Victor_ChatRequest(BaseModel):
    """Incoming request body for a chat message."""

    victor_session_id: str = Field(..., min_length=1, description="Client session identifier")
    victor_message: str = Field(..., min_length=1, description="User message sent to the AI")


class Victor_ChatResponse(BaseModel):
    """Outgoing response returned by the API."""

    victor_session_id: str
    victor_response_id: str
    victor_reply: str
