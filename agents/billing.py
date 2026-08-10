"""Billing Agent - specialized sub-agent for billing and payment topics."""

from google.adk.agents import LlmAgent
from tools.ticket import crear_ticket


AGENT_NAME = "billing_support"
AGENT_DESCRIPTION = (
    "Specialized billing and payments agent. "
    "Handles inquiries about invoices, payment methods, "
    "subscriptions, charges, and account statements."
)
AGENT_INSTRUCTION = """Eres el agente de Facturación.

Tu rol es ayudar al usuario con temas relacionados con dinero y pagos:
- Consultas sobre facturas
- Métodos de pago
- Estado de suscripciones
- Problemas con cobros
- Reembolsos
- Información de precios

Instrucciones:
1. Primero, entiende qué necesita el usuario.
2. Proporciona información clara sobre facturación.
3. Si es un problema que requiere atención humana, crea un ticket.
4. Usa un tono profesional y servicial en español.

Cuando crees un ticket, usa:
- asunto: descripción corta del tema de facturación
- descripcion: detalles completos del problema o consulta
- prioridad: baja (consulta), media (problema de pago), alta (urgente)"""


billing_support_agent = LlmAgent(
    name=AGENT_NAME,
    description=AGENT_DESCRIPTION,
    instruction=AGENT_INSTRUCTION,
    tools=[crear_ticket],
)