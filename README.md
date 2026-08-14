# Support Multi-Agent System (ADK)

A comprehensive multi-agent support system built with the Google Agent Development Kit (ADK). This project leverages large language models (LLMs) to automatically route, diagnose, and resolve user support queries. When human intervention is required, the system automatically creates support tickets and routes them to the appropriate external system based on the issue category.

## Architecture

The system utilizes a hierarchy of specialized agents to ensure accurate responses and clean separation of concerns:

*   **Root / Triage Agent**: The entry point for all queries. It analyzes the user's intent and routes the conversation to the correct specialized sub-agent.
*   **Technical Support Agent**: Handles software issues, code errors, and performance bugs.
*   **Billing Support Agent**: Manages inquiries about invoices, subscriptions, payments, and refunds.

### The Ticket System (Strategy Pattern)

When an agent cannot resolve an issue autonomously, it utilizes the `create_ticket` tool. This tool implements the **Strategy Pattern** to dynamically route tickets to different tracking systems based on the `category`:

1.  **Technical Tickets (`category: technical`)**: Routed to **GitHub Issues** via the GitHub REST API. This ensures developers can track bugs in their natural workflow.
2.  **Billing Tickets (`category: billing`)**: Routed to a **Google Spreadsheet** via the Google Sheets API. This ensures non-technical staff and administrators can manage administrative tasks easily.

The architecture is highly extensible. To add a new provider (e.g., Jira or Zendesk), you simply implement the `TicketProvider` protocol and register it in the `TicketManager`.

### Memory Integration

The system integrates with the ADK's `InMemoryMemoryService`. Every ticket creation attempt generates a `MemoryEntry` that is asynchronously stored in the system. This provides the agent with persistent historical context about the operations it has performed during a session.

## Prerequisites & Setup

### 1. Environment Variables

Create a `.env` file in the root of the project and populate it with your credentials:

```env
# GitHub Configuration (For Technical Tickets)
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_REPO=your_github_username/your_repository_name

# Google Sheets Configuration (For Billing Tickets)
GOOGLE_SHEET_ID=your_google_spreadsheet_id
```

### 2. Google Cloud Service Account

For the Google Sheets integration to work, you must provide a Service Account JSON key:

1.  Go to the Google Cloud Console.
2.  Enable the **Google Sheets API**.
3.  Create a Service Account and download the JSON key.
4.  Rename the file to `google_credentials.json` and place it in the root of the project.
5.  **Important:** Share your target Google Spreadsheet with the email address found inside the `google_credentials.json` file (give it Editor access).

### 3. Installation

Ensure you have Python 3.10+ installed.

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install requests gspread google-auth python-dotenv
```

*(Note: ensure `google.adk` and its dependencies are also properly installed).*

## Usage

To test the multi-agent system and the ticket routing manually, you can run the root agent or test the ticket creation directly:

```bash
export PYTHONPATH=$(pwd)/src
python src/support_app/main.py # Assuming there is an entry point script
```

Or test the ticket creation tool directly using a scratch script:

```python
from support_app.tools.create_ticket import create_ticket

# This will create a GitHub Issue
create_ticket(
    subject="Bug in login page",
    description="The login button is unresponsive on mobile devices.",
    priority="alta",
    category="technical"
)

# This will append a row to Google Sheets
create_ticket(
    subject="Overcharged on last invoice",
    description="My credit card was charged twice for the monthly subscription.",
    priority="media",
    category="billing"
)
```

## Contributing

When modifying the tools or agents, ensure that system prompts remain updated with any parameter changes (always use English parameters such as `subject`, `description`, `priority`, and `category`). 

For new ticket providers, add them to `src/support_app/services/tickets/`.
