"""Application entrypoint for the Support Multi-Agent system.

This module wires the ADK Runner with the correct services so that memory
is properly shared across all agent conversations within a session.
Run with: adk web src/support_app/app.py
"""

from google.adk.apps import App
from google.adk.memory import InMemoryMemoryService
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from .agents.root_agent import root_agent


memory_service = InMemoryMemoryService()
session_service = InMemorySessionService()

app = App(
    name="support_app",
    root_agent=root_agent,
)

runner = Runner(
    app=app,
    session_service=session_service,
    memory_service=memory_service,
)
