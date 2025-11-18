from models.template_data import TemplateData
from services.template_services import TemplateService


def generate_document_tool(data: TemplateData) -> dict:
    """
    MCP Tool: Genera un documento .docx usando TemplateData.
    Recibe un objeto pydantic TemplateData.
    """
    service = TemplateService()
    output_path = service.generate_deployment_doc(data)
    return {
        "status": "success",
        "output_file": output_path
    }