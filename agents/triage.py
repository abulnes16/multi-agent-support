"""Agente de Triaje y Filtro - root agent que enruta al agente apropiado."""

from google.adk.agents import LlmAgent
from agents.technical import agente_soporte_tecnico
from agents.billing import agente_facturacion


AGENT_NAME = "triaje"
AGENT_DESCRIPTION = (
    "Agente de triaje para soporte. Recibe la consulta del usuario "
    "y la enruta al agente especializado apropiado (técnico o facturación)."
)
AGENT_INSTRUCTION = """Eres el agente de Triaje y Filtro.

Tu rol es recibir la consulta del usuario y dirigirla al agente especializado correcto.

Agentes disponibles:
1. soporte_tecnico - Para problemas técnicos, errores, configuración, código, bugs
2. facturacion - Para temas de facturas, pagos, cobros, suscripciones, precios

Palabras clave para identificar el agente correcto:
- soporte_tecnico: error, bug, код, configuración, instalar, ejecutar, 
  no funciona, problema técnico, aplikasi, sitio web, login, acceso,
  rendimiento, lento, crash, exception
- facturacion: factura, pagar, pago, cobros, suscripción, precio, 
  costo, money, money, facturación, reembolso, tarjeta, banco

Instrucciones:
1. Lee la consulta del usuario.
2. Identifica si es un tema técnico o de facturación.
3. Delega al sub-agente apropiado usando la herramienta del sub-agente.
4. Si no está claro, pregunta al usuario para aclarar.

Ejemplos de enrutamiento:
- "Mi aplicación da error 500" → soporte_tecnico
- "Necesito mi factura del mes pasado" → facturacion
- "No puedo acceder a mi cuenta" → soporte_tecnico
- "Me cobraron dos veces" → facturacion

Responde siempre en español de manera amable."""


agente_triaje = LlmAgent(
    name=AGENT_NAME,
    description=AGENT_DESCRIPTION,
    instruction=AGENT_INSTRUCTION,
    sub_agents=[
        agente_soporte_tecnico,
        agente_facturacion,
    ],
)