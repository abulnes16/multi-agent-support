import os
import gspread
from google.oauth2.service_account import Credentials
from typing import Dict, Any
from .provider import TicketProvider

class GoogleSheetsTicketProvider(TicketProvider):
    def create_ticket(self, ticket_id: str, subject: str, description: str, priority: str) -> Dict[str, Any]:
        sheet_id = os.getenv("GOOGLE_SHEET_ID")
        # Go up from src/support_app/services/tickets/sheets_provider.py to root
        creds_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))), 
            "google_credentials.json"
        )
        
        if not sheet_id:
            return {
                "success": False,
                "message": "GOOGLE_SHEET_ID is not configured."
            }
            
        if not os.path.exists(creds_path):
            return {
                "success": False,
                "message": f"Google credentials not found at {creds_path}"
            }
            
        try:
            scopes = [
                'https://www.googleapis.com/auth/spreadsheets',
                'https://www.googleapis.com/auth/drive'
            ]
            creds = Credentials.from_service_account_file(creds_path, scopes=scopes)
            client = gspread.authorize(creds)
            
            sheet = client.open_by_key(sheet_id).sheet1
            # Format: [ID, Subject, Description, Priority, Status]
            row = [ticket_id, subject, description, priority, "created"]
            sheet.append_row(row)
            
            return {
                "success": True,
                "message": "Row appended successfully to Google Sheets."
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error appending to Google Sheets: {str(e)}"
            }
