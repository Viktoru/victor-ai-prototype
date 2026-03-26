# MIT License

# Copyright (c) 2026 Victor

# This file is part of the Class_one_victor_ai project.
# See the LICENSE file in the project root for full license information.

# Service layer that communicates with OpenAI

from __future__ import annotations

from openai import OpenAI

from app.config import victor_get_config


class Victor_OpenAIService:
    # Handles all OpenAI API interactions for the application

    def __init__(self) -> None:
        # Load configuration (API key, model name)
        self.victor_config = victor_get_config()

        # Initialize OpenAI client with API key
        self.victor_client = OpenAI(api_key=self.victor_config.victor_openai_api_key)

    def victor_send_chat_message(
        self,
        victor_user_message: str,
        victor_previous_response_id: str | None = None,
    ):
        # Send a message to OpenAI using the Responses API
        # If previous_response_id is provided, the conversation state is preserved

        # Common parameters for all requests
        victor_common_arguments = {
            "model": self.victor_config.victor_model_name,

            # Instruction defines how the assistant should behave
            "instructions": (
                "You are a clear and practical assistant inside a real Python prototype. "
                "Give direct answers, keep structure clean, and explain steps simply."
            ),
        }

        # If we have a previous response id, continue the conversation
        if victor_previous_response_id:
            return self.victor_client.responses.create(
                **victor_common_arguments,
                previous_response_id=victor_previous_response_id,
                input=[{"role": "user", "content": victor_user_message}],
            )

        # Otherwise, start a new conversation
        return self.victor_client.responses.create(
            **victor_common_arguments,
            input=victor_user_message,
        )