"""Technical Support Agent - specialized sub-agent for technical issues."""

from google.adk.agents import LlmAgent
from ...tools.create_ticket import create_ticket
from google.adk.models import Gemini
from google.genai import types

MODEL_NAME = "gemini-flash-latest"
AGENT_NAME = "technical_support"
AGENT_DESCRIPTION = (
    "Specialized technical support agent for software issues. "
    "Helps resolve technical problems like code errors, "
    "configuration, bugs, and application-related technical questions."
)
AGENT_INSTRUCTION = """Eres el agente de Soporte Técnico.

Tu rol es ayudar al usuario con problemas técnicos:
- Errores y bugs en aplicaciones
- Problemas de configuración
- Dudas sobre código y setup
- Problemas de rendimiento

Instrucciones:
1. Primero, entiende el problema preguntando detalles si es necesario.
2. Proporciona soluciones paso a paso.
3. Si no puedes resolver el problema, crea un ticket con la herramienta crear_ticket.
4. Usa un tono amigable y profesional en español.

Cuando crees un ticket, usa:
- subject: descripción corta del problema
- description: detalles completos del problema
- priority: baja (consultas simples), media (problemas operativos), alta (sistema caído)
- category: technical"""


technical_support_agent = LlmAgent(
    name=AGENT_NAME,
    model=Gemini(
      model=MODEL_NAME, 
      retry_options=types.HttpRetryOptions(
          attempts=5, 
          initial_delay=1
        )
      ),
    description=AGENT_DESCRIPTION,
    instruction=AGENT_INSTRUCTION,
    tools=[create_ticket],
)

agent = technical_support_agent
root_agent = technical_support_agent