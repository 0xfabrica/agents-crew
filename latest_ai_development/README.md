# AI Tutor Crew

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![crewAI](https://img.shields.io/badge/crewAI-blue?style=for-the-badge)](https://www.crewai.com/)
[![Gradio](https://img.shields.io/badge/Gradio-orange?style=for-the-badge&logo=gradio&logoColor=white)](https://www.gradio.app/)
[![FastAPI](https://img.shields.io/badge/FastAPI-05998b?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-blue?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-yellow?style=for-the-badge)](https://huggingface.co/spaces)

Welcome to the AI Tutor Crew, a multi-agent AI system powered by [crewAI](https://crewai.com). This project provides a team of AI agents that work together to answer questions about AI, Machine Learning, and Data Science.

This project is fully containerized with Docker and ready for deployment on Hugging Face Spaces.

## Features

*   **Multi-Agent System:** A team of specialized AI agents (Orchestrator, Web Recon, Academic Researcher, Code Synthesist, and Lead Tutor) collaborate to provide comprehensive answers.
*   **Gradio Interface:** A user-friendly chat interface to interact with the AI Tutor Crew.
*   **FastAPI Endpoint:** An API endpoint to programmatically interact with the crew.
*   **Dockerized:** Comes with a `Dockerfile` for easy and consistent deployment.

## Getting Started

### Prerequisites

*   [Docker](https://www.docker.com/get-started)
*   [Git](https://git-scm.com/downloads)
*   [Python](https://www.python.org/downloads/) >= 3.10

### Running with Docker (Recommended)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/0xfabrica/agents-crew.git
    cd latest_ai_development
    ```

2.  **Build the Docker image:**
    ```bash
    docker build -t ai-tutor-crew .
    ```

3.  **Run the Docker container:**
    You will need to provide your OpenAI API key.
    ```bash
    docker run -p 7860:7860 -e OPENAI_API_KEY="your_openai_api_key" ai-tutor-crew
    ```

4.  **Access the application:**
    Open your web browser and go to `http://localhost:7860`.

### Local Development (Without Docker)

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/0xfabrica/agents-crew.git
    cd latest_ai_development
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root of the project and add your API keys:
    ```
    OPENAI_API_KEY="your_openai_api_key"
    PERPLEXITY_API_KEY="your_perplexity_api_key"
    ```

5.  **Run the application:**
    You can run either the Gradio app or the FastAPI server.

    *   **Gradio App:**
        ```bash
        python app.py
        ```
        Access it at `http://localhost:7860`.

    *   **FastAPI Server:**
        ```bash
        uvicorn server:app --reload
        ```
        Access the API docs at `http://localhost:8000/docs`.

## Deployment on Hugging Face Spaces

This project is ready to be deployed on Hugging Face Spaces.

1.  **Create a new Space:**
    On the Hugging Face website, create a new Space and choose "Docker" as the SDK.

2.  **Upload your files:**
    Upload all the project files to the Space repository.

3.  **Set secrets:**
    In your Space settings, add your `OPENAI_API_KEY` and `PERPLEXITY_API_KEY` as secrets.

Hugging Face will automatically build the Docker image and start the application.

## Project Structure

```
.
├── app.py              # Gradio web interface
├── server.py           # FastAPI server
├── Dockerfile          # Docker configuration
├── requirements.txt    # Python dependencies
├── respuesta.md        # Example output file
├── src/
│   └── latest_ai_development/
│       ├── crew.py     # Agent and task definitions
│       ├── config/     # Agent and task configurations
│       └── tools/      # Custom tools for the agents
└── ...
```
