from typing import Protocol, Dict, Any

class TicketProvider(Protocol):
    """Interface for ticket providers."""
    
    def create_ticket(self, ticket_id: str, subject: str, description: str, priority: str) -> Dict[str, Any]:
        """Creates a ticket and returns a dictionary with the result (success and message)."""
        ...
