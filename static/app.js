// MIT License

// Copyright (c) 2026 Victor

// This file is part of the Class_one_victor_ai project.
// See the LICENSE file in the project root for full license information.

const victor_sessionIdInput = document.getElementById("victor_session_id");
const victor_messageInput = document.getElementById("victor_message");
const victor_sendButton = document.getElementById("victor_send_button");
const victor_clearButton = document.getElementById("victor_clear_button");
const victor_output = document.getElementById("victor_output");
const victor_status = document.getElementById("victor_status");

async function victor_sendMessage() {
    const victor_sessionId = victor_sessionIdInput.value.trim();
    const victor_message = victor_messageInput.value.trim();

    if (!victor_sessionId || !victor_message) {
        victor_status.textContent = "Please add both a session id and a message.";
        return;
    }

    victor_status.textContent = "Sending message to the API...";
    victor_output.textContent = "Waiting for reply...";

    try {
        const victor_response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                victor_session_id: victor_sessionId,
                victor_message: victor_message
            })
        });

        const victor_data = await victor_response.json();

        if (!victor_response.ok) {
            throw new Error(victor_data.detail || "Unknown server error");
        }

        victor_output.textContent = victor_data.victor_reply;
        victor_status.textContent = `Success. Response id: ${victor_data.victor_response_id}`;
    } catch (victor_error) {
        victor_output.textContent = "No reply available.";
        victor_status.textContent = `Error: ${victor_error.message}`;
    }
}

async function victor_clearSession() {
    const victor_sessionId = victor_sessionIdInput.value.trim();

    if (!victor_sessionId) {
        victor_status.textContent = "Please add a session id before clearing.";
        return;
    }

    victor_status.textContent = "Clearing saved session...";

    try {
        const victor_response = await fetch(`/chat/${encodeURIComponent(victor_sessionId)}`, {
            method: "DELETE"
        });

        const victor_data = await victor_response.json();

        if (!victor_response.ok) {
            throw new Error(victor_data.detail || "Unknown server error");
        }

        victor_output.textContent = "Conversation state removed for this session.";
        victor_status.textContent = `Session cleared: ${victor_data.victor_session_id}`;
    } catch (victor_error) {
        victor_status.textContent = `Error: ${victor_error.message}`;
    }
}

victor_sendButton.addEventListener("click", victor_sendMessage);
victor_clearButton.addEventListener("click", victor_clearSession);
