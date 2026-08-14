"""Support ticket creation tool."""

import uuid
from typing import Any
from dotenv import load_dotenv
from google.adk.memory import InMemoryMemoryService, memory_entry

load_dotenv()

from ..services.tickets.manager import TicketManager

# Global instance of TicketManager
ticket_manager = TicketManager()

# Global instance of MemoryService (for demonstration purposes as requested)
memory_service = InMemoryMemoryService()

def create_ticket(subject: str, description: str, priority: str = "media", category: str = "general") -> dict[str, Any]:
    """Creates a support ticket in the system.

    Args:
        subject: Short title of the issue.
        description: Detailed description of the issue.
        priority: Priority level (baja=low, media=medium, alta=high).
        category: The category of the ticket ('technical' or 'billing').

    Returns:
        Dict with the created ticket ID, status, and messages.
    """
    ticket_id = str(uuid.uuid4())[:8]
    print(f"\n[TICKET CREATED] ID: {ticket_id}")
    print(f"  Subject: {subject}")
    print(f"  Priority: {priority}")
    print(f"  Category: {category}")
    print(f"  Description: {description[:100]}...")

    # Delegate to the TicketManager
    result = ticket_manager.create_ticket(ticket_id, subject, description, priority, category)
    
    # Construct response for the agent
    response = {
        "ticket_id": ticket_id,
        "subject": subject,
        "priority": priority,
        "category": category,
        "estado": "creado" if result.get("success") else "error",
        "message": result.get("message", "Unknown error")
    }
    
    print(f"  -> {result.get('message')}")
    
    # Save to ADK memory service
    try:
        import asyncio
        # Format for Content (assuming standard Gemini Content schema)
        content_dict = {"parts": [{"text": f"Ticket {ticket_id} created in category {category}: {result.get('message')}"}], "role": "user"}
        entry = memory_entry.MemoryEntry(content=content_dict)
        asyncio.run(memory_service.add_memory(
            app_name="support_app",
            user_id="system",
            memories=[entry]
        ))
        print("  -> Information saved to ADK MemoryService.")
    except Exception as e:
        print(f"  -> Warning: Could not save to memory service: {e}")

    return response