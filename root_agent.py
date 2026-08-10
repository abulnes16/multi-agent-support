"""Root agent que conecta todos los componentes del sistema multi-agente."""

from google.adk.agents import LlmAgent
from agents.triage import agente_triaje
from tools.ticket import crear_ticket


ROOT_AGENT_NAME = "asistente_soporte"
ROOT_AGENT_DESCRIPTION = (
    "Asistente principal de soporte que recibe consultas de usuarios "
    "y las enruta a agentes especializados en técnico o facturación."
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


# Root agent que usa el agente de triaje como sub-agent
root_agent = LlmAgent(
    name=ROOT_AGENT_NAME,
    description=ROOT_AGENT_DESCRIPTION,
    instruction=ROOT_AGENT_INSTRUCTION,
    sub_agents=[agente_triaje],
    tools=[crear_ticket],
)