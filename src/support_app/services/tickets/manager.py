from typing import Dict, Any
from .provider import TicketProvider
from .github_provider import GitHubTicketProvider
from .sheets_provider import GoogleSheetsTicketProvider

class TicketManager:
    def __init__(self):
        self._providers: Dict[str, TicketProvider] = {
            "technical": GitHubTicketProvider(),
            "billing": GoogleSheetsTicketProvider()
        }
        
    def get_provider(self, category: str) -> TicketProvider:
        """Get the appropriate provider for the category, defaulting to GitHub."""
        return self._providers.get(category, self._providers["technical"])
        
    def create_ticket(self, ticket_id: str, subject: str, description: str, priority: str, category: str) -> Dict[str, Any]:
        provider = self.get_provider(category)
        return provider.create_ticket(ticket_id, subject, description, priority)
