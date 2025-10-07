from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type, ClassVar
from openai import OpenAI # <-- CAMBIO: Usamos la librería de OpenAI
import os

# --- Input Schema (sin cambios) ---
class GeneralSearchToolInput(BaseModel):
    """Input schema for the General Web Search Tool."""
    question: str = Field(
        ...,
        description="The simple question or keyword for a general web search."
    )

# --- Tool Definition (Adaptada al modo de compatibilidad de OpenAI) ---
class GeneralWebSearchTool(BaseTool):
    name: str = "General Web Search Tool"
    description: str = (
        "A fast, general-purpose web search tool. Use it for quick facts, common knowledge, "
        "and general lookups that do not require deep analysis or scholarly sources."
    )
    args_schema: Type[BaseModel] = GeneralSearchToolInput
    
    # CAMBIO: Usamos el modelo 'sonar-pro' como indica la documentación de compatibilidad
    MODEL_NAME: ClassVar[str] = "sonar-pro"

    def _run(self, question: str) -> str:
        """Performs a general web search using the OpenAI-compatible Perplexity API."""
        api_key = os.getenv("PERPLEXITY_API_KEY")
        if not api_key:
            return "ERROR: PERPLEXITY_API_KEY environment variable not set."

        try:
            # CAMBIO: Instanciamos el cliente de OpenAI apuntando a la URL de Perplexity
            client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")
            
            # La llamada a la API ahora usa el cliente de OpenAI
            # No se necesita 'extra_body' porque la búsqueda web es el modo por defecto.
            response = client.chat.completions.create(
                model=self.MODEL_NAME,
                messages=[
                    {"role": "user", "content": question}
                ]
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error executing General Web Search: {e}"