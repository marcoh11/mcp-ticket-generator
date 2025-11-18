from mcp.server.fastmcp import FastMCP
from mcp_config.tools.generate_document_tool import generate_document_tool
from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.middleware.cors import CORSMiddleware
from models.template_data import TemplateData
import uvicorn

mcp = FastMCP("deployment-template-generator")

@mcp.tool()
def generate_document(data: TemplateData):
    """
    Genera un documento Word de deployment basado en una plantilla.
    Args:
        data: Datos completos del deployment validados por Pydantic
    Returns:
        dict: Status y ruta del archivo generado
    """
    return generate_document_tool(data)

app = Starlette(
    routes=[
        Mount('/', app=mcp.sse_app()),
    ]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)