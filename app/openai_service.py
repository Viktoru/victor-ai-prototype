"""Service layer that talks to OpenAI."""

from __future__ import annotations

from openai import OpenAI

from app.config import victor_get_config


class Victor_OpenAIService:
    """Wraps all OpenAI API calls used by the project."""

    def __init__(self) -> None:
        self.victor_config = victor_get_config()
        self.victor_client = OpenAI(api_key=self.victor_config.victor_openai_api_key)

    def victor_send_chat_message(
        self,
        victor_user_message: str,
        victor_previous_response_id: str | None = None,
    ):
        """Send a chat message to OpenAI using the Responses API.

        Args:
            victor_user_message: The user message to send.
            victor_previous_response_id: The previous response id to preserve state.

        Returns:
            The raw OpenAI response object.
        """

        victor_common_arguments = {
            "model": self.victor_config.victor_model_name,
            "instructions": (
                "You are a clear and practical assistant inside a real Python prototype. "
                "Give direct answers, keep structure clean, and explain steps simply."
            ),
        }

        if victor_previous_response_id:
            return self.victor_client.responses.create(
                **victor_common_arguments,
                previous_response_id=victor_previous_response_id,
                input=[{"role": "user", "content": victor_user_message}],
            )

        return self.victor_client.responses.create(
            **victor_common_arguments,
            input=victor_user_message,
        )
