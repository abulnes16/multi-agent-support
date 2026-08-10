"""Agentes del sistema de soporte multi-agente."""

from agents.technical import agente_soporte_tecnico
from agents.billing import agente_facturacion
from agents.triage import agente_triaje

__all__ = [
    "agente_soporte_tecnico",
    "agente_facturacion",
    "agente_triaje",
]