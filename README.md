# victor-ai-prototype

A Python-based AI application prototype built using OpenAI API and FastAPI, featuring conversation state management, session handling, and a scalable backend architecture.

## Overview

This project demonstrates how to build a simple AI-powered chat application using the official OpenAI API and FastAPI.

All core concepts and implementation patterns are based on OpenAI's official documentation:
https://developers.openai.com/api/docs

The goal is to show that with the available documentation and tools, there is no barrier to building a functional AI application quickly.

## What is inside

- FastAPI backend
- Simple HTML + JavaScript frontend
- In-memory session store for local prototype testing
- Clear and structured code
- `.env.example` configuration template
- `instructions.txt` for setup

## Main idea

The application uses OpenAI's Responses API with `previous_response_id` to maintain conversation state.

For each session:
- The app stores the last `response.id`
- On the next request, it sends that ID as `previous_response_id`
- This allows the conversation to continue without manually sending full message history

## Run locally

Follow the steps in `instructions.txt` to set up and run the application on your local machine.

You will need:
- Python 3.9+
- An OpenAI API key

After setup, you can run the app and interact with it in your browser.

## Notes

This is a prototype designed for learning and demonstration purposes.  
It can be extended with:
- persistent storage (database)
- authentication
- deployment to cloud services
- more advanced AI workflows