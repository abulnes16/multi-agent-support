"""Technical Support Agent - specialized sub-agent for technical issues."""

from google.adk.agents import LlmAgent
from tools.ticket import create_ticket


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
- asunto: descripción corta del problema
- descripcion: detalles completos del problema
- prioridad: baja (consultas simples), media (problemas operativos), alta (sistema caído)"""


technical_support_agent = LlmAgent(
    name=AGENT_NAME,
    description=AGENT_DESCRIPTION,
    instruction=AGENT_INSTRUCTION,
    tools=[create_ticket],
)