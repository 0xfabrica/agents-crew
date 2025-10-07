# Imports necesarios
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type, ClassVar
from openai import OpenAI
import os


# --- Input Schema ---
class DeepResearchToolInput(BaseModel):
    """Input schema."""
    question: str = Field(
        ...,
        description="The detailed question or complex topic for the deep, multi-source research in academic sources.",
    )
    
class DeepResearchTool(BaseTool):
    name: str = "Deep Academic Research Tool"
    description: str = (
        "An advanced research tool that performs exhaustive web searches focused on peer-reviewed and scholarly sources. "
        "Use it for complex questions that require detailed analysis and reliable scientific evidence."
    )
    args_schema: Type[BaseModel] = DeepResearchToolInput
    
    MODEL_NAME: ClassVar[str] = "sonar-pro"

    def _run(self, question: str) -> str:
        """Performs an academic deep search using the OpenAI-compatible Perplexity API."""
        api_key = os.getenv("PERPLEXITY_API_KEY")
        if not api_key:
            return "ERROR: PERPLEXITY_API_KEY environment variable not set."

        try:
            client = OpenAI(api_key=api_key, base_url="https://api.perplexity.ai")
            
            # La llamada a la API ahora usa el cliente de OpenAI
            response = client.chat.completions.create(
                model=self.MODEL_NAME,
                messages=[
                    {"role": "user", "content": question}
                ],
                # CAMBIO CLAVE: Los parámetros de Perplexity van en 'extra_body'
                extra_body={
                    "search_mode": "academic",
                }
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error executing Academic Deep Research: {e}"