from fastapi import FastAPI
from pydantic import BaseModel
from src.latest_ai_development.crew import IaTutorCrew
from dotenv import load_dotenv
import os

# Carga las variables del archivo .env
load_dotenv()

# Define el modelo de datos para la pregunta de entrada
class Question(BaseModel):
    query: str

# Inicializa la aplicación FastAPI
app = FastAPI(
    title="API del Tutor de IA con CrewAI",
    description="Una API para hacer preguntas a una crew de agentes expertos en IA."
)

# Instancia la crew una sola vez al iniciar el servidor
tutor_crew = IaTutorCrew().crew()

@app.get("/")
def read_root():
    return {"status": "El servidor del Tutor de IA está activo."}

@app.post("/ask", response_model=dict)
def ask_question(question: Question):
    """
    Recibe una pregunta y la procesa con la crew de CrewAI.
    """
    inputs = {'user_question': question.query}

    # Ejecuta la crew y captura el resultado
    result = tutor_crew.kickoff(inputs=inputs)

    return {"answer": result}