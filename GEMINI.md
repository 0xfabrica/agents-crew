# Project Overview

This project is a multi-agent AI system built with the [crewAI](https://crewai.com) framework. It functions as an "AI Tutor" that can answer questions about AI, Machine Learning, and Data Science. The system is composed of a team of AI agents, each with a specialized role, that collaborate to provide a comprehensive answer to a user's question.

The project includes two interfaces for interacting with the AI agents:

*   A **Gradio web interface** (`app.py`) for a chat-based interaction.
*   A **FastAPI server** (`server.py`) that exposes an API endpoint for programmatic access.

The core logic, including agent and task definitions, is located in the `src/latest_ai_development` directory. The agents and tasks are configured in `src/latest_ai_development/config/agents.yaml` and `src/latest_ai_development/config/tasks.yaml` respectively.

## Building and Running

This project uses `uv` for dependency management.

**Installation:**

1.  Install `uv`:
    ```bash
    pip install uv
    ```
2.  Install project dependencies:
    ```bash
    uv pip install -r requirements.txt
    ```
    *(Note: The `README.md` mentions `crewai install`, but `requirements.txt` is a more standard approach if `crewai install` is not available.)*

**Running the Application:**

You can run the project in two ways:

1.  **Gradio Web Interface:**
    ```bash
    python app.py
    ```
2.  **FastAPI Server:**
    ```bash
    uvicorn server:app --reload
    ```

## Development Conventions

*   **Agent and Task Configuration:** Agents and tasks are defined in `src/latest_ai_development/config/agents.yaml` and `src/latest_ai_development/config/tasks.yaml`. The `src/latest_ai_development/crew.py` file loads these configurations and assembles the crew.
*   **Tools:** Custom tools for the agents are located in the `src/latest_ai_development/tools` directory.
*   **Entry Points:** The main entry points for the application are `app.py` (Gradio) and `server.py` (FastAPI).
*   **Dependencies:** Project dependencies are managed with `uv` and are listed in `pyproject.toml`.
