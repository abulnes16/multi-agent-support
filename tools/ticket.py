"""Tool para crear tickets de soporte."""

import uuid
from typing import Any


def crear_ticket(asunto: str, descripcion: str, prioridad: str = "media") -> dict[str, Any]:
    """Crea un ticket de soporte en el sistema.

    Args:
        asunto: Titulo corto del problema.
        descripcion: Descripcion detallada del problema.
        prioridad: Nivel de prioridad del ticket (baja, media, alta).

    Returns:
        Dict con el ID del ticket creado y su estado.
    """
    ticket_id = str(uuid.uuid4())[:8]
    print(f"\n[TICKET CREADO] ID: {ticket_id}")
    print(f"  Asunto: {asunto}")
    print(f"  Prioridad: {prioridad}")
    print(f"  Descripcion: {descripcion[:100]}...")

    return {
        "ticket_id": ticket_id,
        "asunto": asunto,
        "prioridad": prioridad,
        "estado": "creado"
    }