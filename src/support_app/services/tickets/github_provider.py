import os
import requests
from typing import Dict, Any
from .provider import TicketProvider

class GitHubTicketProvider(TicketProvider):
    def create_ticket(self, ticket_id: str, subject: str, description: str, priority: str) -> Dict[str, Any]:
        github_token = os.getenv("GITHUB_TOKEN")
        github_repo = os.getenv("GITHUB_REPO")
        
        if not github_token or not github_repo:
            return {
                "success": False,
                "message": "GITHUB_TOKEN or GITHUB_REPO is not configured."
            }
            
        url = f"https://api.github.com/repos/{github_repo}/issues"
        headers = {
            "Authorization": f"Bearer {github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        data = {
            "title": f"[{priority.upper()}] {subject}",
            "body": f"**Ticket ID:** {ticket_id}\n**Priority:** {priority}\n\n{description}",
            "labels": ["technical-support", priority]
        }
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            html_url = response.json().get('html_url')
            return {
                "success": True,
                "message": f"GitHub Issue created successfully: {html_url}",
                "url": html_url
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error creating GitHub Issue: {str(e)}"
            }
