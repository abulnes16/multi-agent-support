"""Agente de Soporte Técnico - sub-agente especializado en problemas técnicos."""

from google.adk.agents import LlmAgent
from tools.ticket import crear_ticket


AGENT_NAME = "soporte_tecnico"
AGENT_DESCRIPTION = (
    "Agente especializado en soporte técnico de software. "
    "Ayuda a resolver problemas técnicos como errores de código, "
    "configuración, bugs, y cuestiones técnicas relacionadas con aplicaciones."
)
AGENT_INSTRUCTION = """Eres el agente de Soporte Técnico.

Tu rol es ayudar al usuario con problemas técnicos:
- Errores y bugs en aplicaciones
- Problemas de configuración
- Dudas sobre código
-安装 y setup
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


agente_soporte_tecnico = LlmAgent(
    name=AGENT_NAME,
    description=AGENT_DESCRIPTION,
    instruction=AGENT_INSTRUCTION,
    tools=[crear_ticket],
)