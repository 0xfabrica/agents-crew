# app.py
import gradio as gr
from src.latest_ai_development.crew import IaTutorCrew  # Asegúrate de que la ruta de importación es correcta
from dotenv import load_dotenv

# Cargar las variables de entorno (API keys)
load_dotenv()

print("Initializing Crew... This might take a moment.")
# Instanciamos la crew UNA SOLA VEZ al iniciar la aplicación para mayor eficiencia.
crew_instance = IaTutorCrew().crew()
print("Crew Initialized. Gradio UI is ready.")


def chat_with_crew(message, history):
    """
    Función que Gradio llamará con cada mensaje del usuario.
    """
    print(f"User message: {message}")
    
    # Preparamos el input para la crew
    inputs = {'user_question': message}
    history = history or []
    
    # Ejecutamos la crew y obtenemos el resultado
    # IMPORTANTE: Esto puede tardar, la interfaz esperará hasta que termine.
    result_object = crew_instance.kickoff(inputs=inputs)

    # Extraemos el texto de la respuesta en formato bruto
    final_response_text = result_object.raw
    
    print(f"Crew result: {result_object}")
    
    # Devolvemos el resultado para que Gradio lo muestre
    return final_response_text


# Configuramos la interfaz de chat de Gradio
iface = gr.ChatInterface(
    fn=chat_with_crew,
    title="AI Tutor Crew 🤖",
    description="Chatea con el equipo de agentes expertos en Ciencia de Datos.",
    examples=[
        "Explain the difference between classification and regression",
        "Give me a Python code example for a simple neural network using PyTorch"
    ],
    chatbot=gr.Chatbot(height=600, type="messages"),
)

# Lanzamos la interfaz
if __name__ == "__main__":
    iface.launch(share=True)  # share=True para obtener un enlace público temporal

# This share link expires in 1 week. 
# For free permanent hosting and GPU upgrades,
# run `gradio deploy` from the terminal in the working directory 
# to deploy to Hugging Face Spaces (https://huggingface.co/spaces)