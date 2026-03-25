# victor-ai-prototype
A Python-based AI application prototype using OpenAI API and FastAPI, featuring conversation state management, session handling, and a scalable backend architecture.
=======
# Class_one_victor_ai

Class_one_victor_ai is a small FastAPI prototype that uses OpenAI's Responses API to build a simple chat application with conversation state.

## What is inside

- FastAPI backend
- Simple HTML + JavaScript frontend
- In-memory session store for local prototype testing
- Clear comments in the code
- .env.example template
- instructions.txt

## Main idea

The app saves the last OpenAI response.id for each session id.
When the same session sends another message, the app passes that saved id back as previous_response_id.
That keeps the conversation connected without manually sending the full message history each time.

## Project structure


Class_one_victor_ai/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── models.py
│   ├── openai_service.py
│   └── store.py
├── static/
│   ├── app.js
│   └── style.css
├── templates/
│   └── index.html
├── .env.example
├── .gitignore
├── instructions.txt
├── README.md
└── requirements.txt


## Run
See instructions.txt for step-by-step setup on a local machine.