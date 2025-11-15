import os
import time
from docxtpl import DocxTemplate
from models.template_data import TemplateData

class TemplateService:

    TEMPLATE_PATH = "templates/ticket_production_template.docx"
    OUTPUT_DIR = "outputs"

    def __init__(self):
        os.makedirs(self.OUTPUT_DIR, exist_ok=True)

    def generate_deployment_doc(self, data: TemplateData) -> str:
        """
        Genera un archivo Word basado en TemplateData
        y lo guarda en /outputs con formato:
        Deployment_file_<timestamp>.docx
        """
        doc = DocxTemplate(self.TEMPLATE_PATH)
        context = data.dict()
        doc.render(context)
        timestamp = int(time.time())  
        file_name = f"Deployment_file_{timestamp}.docx"
        output_path = os.path.join(self.OUTPUT_DIR, file_name)

        doc.save(output_path)

        return output_path
