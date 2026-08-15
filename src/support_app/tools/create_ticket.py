"""Support ticket creation tool."""

import uuid
from typing import Any
from dotenv import load_dotenv

load_dotenv()

from ..services.tickets.manager import TicketManager

# Global instance of TicketManager
ticket_manager = TicketManager()


def create_ticket(subject: str, description: str, priority: str = "media", category: str = "general") -> dict[str, Any]:
    """Creates a support ticket in the system.

    Args:
        subject: Short title of the issue.
        description: Detailed description of the issue.
        priority: Priority level (baja=low, media=medium, alta=high).
        category: The category of the ticket ('technical' or 'billing').

    Returns:
        Dict with the created ticket ID, status, and a message for the agent
        to relay to the user (success URL or error reason).
    """
    ticket_id = str(uuid.uuid4())[:8]
    print(f"\n[TICKET CREATED] ID: {ticket_id}")
    print(f"  Subject: {subject}")
    print(f"  Priority: {priority}")
    print(f"  Category: {category}")
    print(f"  Description: {description[:100]}...")

    # Delegate to the TicketManager
    result = ticket_manager.create_ticket(ticket_id, subject, description, priority, category)

    print(f"  -> {result.get('message')}")

    return {
        "ticket_id": ticket_id,
        "subject": subject,
        "priority": priority,
        "category": category,
        "status": "created" if result.get("success") else "error",
        "message": result.get("message", "Unknown error"),
    }