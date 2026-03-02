# Multi-Agent Research Assistant
Simple multi-agent research assistant that answers user questions using multiple AI agents working together.

## Overview
A Research assistant using:
1. LangGraph to orchestrate agents
2. Mock MCP (Model Context Protocol) tool
3. Django REST API as backend
4. Streamlit UI as frontend
5. Database to store conversations (SQLite)

The goal is to demonstrate agent collaboration, tool usage via MCP, and a basic full-stack setup.

## How it Works / Flow Diagram
User > Streamlit UI > Django API > Planner Agent > Research Agent > MCP Tool > Final Answer > Stored in Database > Displayed in UI

## Dependencies Installation
1. All the dependencies are in requirements.txt
2. Run the "pip install -r requirements.txt" in terminal environment.

## How to Run
1. Create and activate virtual environment
2. Install requirements, dependencies
3. Run Django backend in backend/server:
    python manage.py migrate    >   python manage.py runserver

    Syncs your Database, runs the Django server.
4. Run Streamlit UI:
    streamlit run app.py

    Runs the UI and enables the access over it.

## Examples
Question: Capital of Germany?

Answer: The capital of Germany is Berlin.

Question: Tell me the capital of India.

Answer: The capital of India is New Delhi.