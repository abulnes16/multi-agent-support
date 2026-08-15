"""Billing Agent - specialized sub-agent for billing and payment topics."""

from google.adk.agents import LlmAgent
from ...tools.create_ticket import create_ticket
from google.adk.models import Gemini
from google.genai import types

MODEL_NAME = "gemini-flash-latest"
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
- subject: descripción corta del tema de facturación
- description: detalles completos del problema o consulta
- priority: baja (consulta), media (problema de pago), alta (urgente)
- category: billing"""


billing_support_agent = LlmAgent(
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

agent = billing_support_agent
root_agent = billing_support_agent