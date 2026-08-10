"""
Entry point para ejecutar el sistema multi-agente con ADK Web.

Uso:
    python app.py

Esto inicia el servidor web de ADK en http://localhost:8000
"""

import os
import sys

# Agregar el directorio actual al path para imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from google.adk.cli.fast_api import get_fast_api_app
from root_agent import root_agent


def main():
    """Inicia el servidor web de ADK."""
    # Obtener la app FastAPI con nuestro agente
    app = get_fast_api_app(
        agents_dir=os.path.dirname(os.path.abspath(__file__)),
        web=True,
        host="127.0.0.1",
        port=8000,
    )
    
    print("\n" + "="*60)
    print("🎫 Sistema de Soporte Multi-Agente ADK")
    print("="*60)
    print("\n📍 Servidor iniciado en: http://127.0.0.1:8000")
    print("\n📋 Endpoints disponibles:")
    print("   - GET  /             → Interfaz web de ADK")
    print("   - GET  /health       → Health check")
    print("   - WebSocket /ws      → Comunicación en tiempo real")
    print("\n🧪 Para probar:")
    print('   1. Abre http://127.0.0.1:8000 en tu navegador')
    print('   2. Selecciona el agente "asistente_soporte"')
    print('   3. Envía un mensaje en español')
    print("\n" + "="*60 + "\n")
    
    # Importar uvicorn para ejecutar el servidor
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()