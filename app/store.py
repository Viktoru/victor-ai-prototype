# MIT License

# Copyright (c) 2026 Victor

# This file is part of the Class_one_victor_ai project.
# See the LICENSE file in the project root for full license information.

# Simple in-memory session store for conversation state
# Used for local testing and prototypes
# For production, replace with Redis, Postgres, or another persistent store

from __future__ import annotations

from typing import Dict, Optional


class Victor_SessionStore:
    # Stores the last OpenAI response id for each session

    def __init__(self) -> None:
        # Dictionary mapping session_id -> response_id
        self.victor_sessions: Dict[str, str] = {}

    def victor_get_previous_response_id(self, victor_session_id: str) -> Optional[str]:
        # Return the last response id for a session (if it exists)

        return self.victor_sessions.get(victor_session_id)

    def victor_set_previous_response_id(
        self, victor_session_id: str, victor_response_id: str
    ) -> None:
        # Save the latest response id for a session

        self.victor_sessions[victor_session_id] = victor_response_id

    def victor_clear_session(self, victor_session_id: str) -> None:
        # Remove session data if it exists

        self.victor_sessions.pop(victor_session_id, None)