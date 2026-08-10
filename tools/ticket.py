"""Support ticket creation tool."""

import uuid
from typing import Any


def create_ticket(asunto: str, descripcion: str, prioridad: str = "media") -> dict[str, Any]:
    """Creates a support ticket in the system.

    Args:
        asunto: Short title of the issue.
        descripcion: Detailed description of the issue.
        prioridad: Priority level (baja=low, media=medium, alta=high).

    Returns:
        Dict with the created ticket ID and status.
    """
    ticket_id = str(uuid.uuid4())[:8]
    print(f"\n[TICKET CREATED] ID: {ticket_id}")
    print(f"  Asunto: {asunto}")
    print(f"  Prioridad: {prioridad}")
    print(f"  Descripcion: {descripcion[:100]}...")

    return {
        "ticket_id": ticket_id,
        "asunto": asunto,
        "prioridad": prioridad,
        "estado": "creado"
    }


# Keep Spanish alias for compatibility with agent instructions
crear_ticket = create_ticket