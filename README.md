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
1. Python setup and an active virtual environment is a prerequisite.
```bash
python -m venv venv
venv\Scripts\activate
```
2. All the other dependencies for it are in the requirements.txt file.
3. Run the below command in terminal to install the requirements:
```bash
pip install -r requirements.txt
```

## How to Run
1. A virtual environment is already created in Dependencies Installation.
2. Install requirements, dependencies. (Refer above)
3. Run Django backend (backend/server)
```bash
python manage.py migrate
python manage.py runserver
```
4. Run Streamlit UI (Runs the UI and enables the access over it):
```bash
    streamlit run app.py
```

## Examples
Question: Capital of Germany?

Answer: The capital of Germany is Berlin.

Question: Tell me the capital of India.

Answer: The capital of India is New Delhi.