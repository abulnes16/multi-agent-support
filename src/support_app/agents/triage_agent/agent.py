"""Triage and Filter Agent - root agent that routes to the appropriate specialized agent."""

from google.adk.agents import LlmAgent
from ..technical_support.agent import technical_support_agent
from ..billing_support.agent import billing_support_agent
from ...tools.create_ticket import create_ticket


AGENT_NAME = "triage_agent"
AGENT_DESCRIPTION = (
    "Triage agent for support. Receives user query "
    "and routes to the appropriate specialized agent (technical or billing)."
)
AGENT_INSTRUCTION = """Eres el agente de Triaje y Filtro.

Tu rol es recibir la consulta del usuario y dirigirla al agente especializado correcto.

Agentes disponibles:
1. technical_support - Para problemas técnicos, errores, configuración, código, bugs
2. billing_support - Para temas de facturas, pagos, cobros, suscripciones, precios

Palabras clave para identificar el agente correcto:
- technical_support: error, bug, código, configuración, instalar, ejecutar, 
  no funciona, problema técnico, aplicación, sitio web, login, acceso,
  rendimiento, lento, crash, exception
- billing_support: factura, pagar, pago, cobros, suscripción, precio, 
  costo, dinero, facturación, reembolso, tarjeta, banco

Instrucciones:
1. Lee la consulta del usuario.
2. Identifica si es un tema técnico o de facturación.
3. Delega al sub-agente apropiado usando la herramienta del sub-agente.
4. Si no está claro, pregunta al usuario para aclarar.

Ejemplos de enrutamiento:
- "Mi aplicación da error 500" → technical_support
- "Necesito mi factura del mes pasado" → billing_support
- "No puedo acceder a mi cuenta" → technical_support
- "Me cobraron dos veces" → billing_support

Responde siempre en español de manera amable."""

triage_agent = LlmAgent(
    name=AGENT_NAME,
    description=AGENT_DESCRIPTION,
    instruction=AGENT_INSTRUCTION,
    sub_agents=[
        technical_support_agent,
        billing_support_agent,
    ],
    tools=[create_ticket],
)

agent = triage_agent
root_agent = triage_agent