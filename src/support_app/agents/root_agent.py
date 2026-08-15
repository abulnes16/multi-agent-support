"""Root agent that connects all components of the multi-agent system."""

from google.adk.agents import LlmAgent
from .triage_agent.agent import triage_agent
from ..tools.create_ticket import create_ticket
from google.adk.models import Gemini
from google.genai import types


MODEL_NAME = "gemini-flash-latest"
ROOT_AGENT_NAME = "support_assistant"
ROOT_AGENT_DESCRIPTION = (
    "Main support assistant that receives user queries "
    "and routes them to specialized agents (technical or billing)."
)
ROOT_AGENT_INSTRUCTION = """Eres el asistente principal de soporte.

Tu rol es ser el primer punto de contacto con el usuario:
1. Saluda de manera amable y pregunta en qué puedes ayudar.
2. Recibe la consulta del usuario.
3. Usa el agente de triaje para dirigir la consulta al especialista apropiado.

Dispones de:
- Agente de triaje: detecta si el tema es técnico o de facturación
- Tool crear_ticket: para crear tickets de soporte cuando sea necesario

Siempre responde en español de manera profesional."""

root_agent = LlmAgent(
    name=ROOT_AGENT_NAME,
    model=Gemini(
      model=MODEL_NAME, 
      retry_options=types.HttpRetryOptions(
          attempts=5, 
          initial_delay=1
        )
      ),
    description=ROOT_AGENT_DESCRIPTION,
    instruction=ROOT_AGENT_INSTRUCTION,
    sub_agents=[triage_agent],
    tools=[create_ticket],
)

agent = root_agent