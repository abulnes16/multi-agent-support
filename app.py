"""
Entry point to run the multi-agent system with ADK Web.

Usage:
    python app.py

This starts the ADK web server at http://localhost:8000
"""

import os
import sys

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from google.adk.cli.fast_api import get_fast_api_app
from root_agent import root_agent


def main():
    """Starts the ADK web server."""
    # Get FastAPI app with our agent
    app = get_fast_api_app(
        agents_dir=os.path.dirname(os.path.abspath(__file__)),
        web=True,
        host="127.0.0.1",
        port=8000,
    )
    
    print("\n" + "="*60)
    print("Multi-Agent ADK Support System")
    print("="*60)
    print("\nServer started at: http://127.0.0.1:8000")
    print("\nAvailable endpoints:")
    print("   - GET  /             → ADK web interface")
    print("   - GET  /health       → Health check")
    print("   - WebSocket /ws      → Real-time communication")
    print("\nTo test:")
    print('   1. Open http://127.0.0.1:8000 in your browser')
    print('   2. Select agent "support_assistant"')
    print('   3. Send a message in Spanish')
    print("\n" + "="*60 + "\n")
    
    # Import uvicorn to run the server
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()