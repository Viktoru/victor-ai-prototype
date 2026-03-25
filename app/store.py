"""Simple in-memory session store for conversation state.

This is fine for local testing and prototypes.
For production use, replace it with Redis, Postgres, or another shared data store.
"""

from __future__ import annotations

from typing import Dict, Optional


class Victor_SessionStore:
    """Keeps track of the last OpenAI response id per session."""

    def __init__(self) -> None:
        self.victor_sessions: Dict[str, str] = {}

    def victor_get_previous_response_id(self, victor_session_id: str) -> Optional[str]:
        """Return the latest response id for a session, if present."""

        return self.victor_sessions.get(victor_session_id)

    def victor_set_previous_response_id(
        self, victor_session_id: str, victor_response_id: str
    ) -> None:
        """Save the latest response id for a session."""

        self.victor_sessions[victor_session_id] = victor_response_id

    def victor_clear_session(self, victor_session_id: str) -> None:
        """Delete session state if the session exists."""

        self.victor_sessions.pop(victor_session_id, None)
