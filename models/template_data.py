from pydantic import BaseModel, Field
from typing import List, Optional
from .enums import DeploymentType
from .component import Component
from .script import Script
from .rollback_script import RollbackScript
from .step import Step
from .rollback_plan import RollbackPlan
from .verification import Verification
from .approver import Approver

class TemplateData(BaseModel):

    model_config = {
        "use_enum_values": True
    }

    deploymentType: DeploymentType = Field(
        description="Tipo de despliegue (Incidencia,Requerimiento,etc)",
        example="Requerimiento"
    )
    deploymentDate: str = Field(
        description="Fecha del despliegue (DD/MM/YYYY)",
        example="15/02/2025"
    )
    glpiTicketId: int = Field(
        description="ID del ticket GLPI",
        example=12345
    )
    deploymentName: str = Field(
        description="Nombre del despliegue",
        example="Actualización módulo de pagos"
    )
    deploymentRequester: str = Field(
        description="Solicitante del despliegue",
        example="Juan Pérez"
    )
    deploymentDeveloper: str = Field(
        description="Desarrollador responsable",
        example="Ana Torres"
    )
    deploymentApprover: str = Field(
        description="Aprobador del despliegue",
        example="Carlos Soto"
    )
    deploymentDescription: str = Field(
        description="Descripción detallada del despliegue",
        example="Se optimizan consultas SQL en el módulo de pagos"
    )

    flgTests: str = Field(
        description="Flag de pruebas (usar 'X' si aplica)",
        example="X",
        default=""
    )
    flgRollback: str = Field(
        description="Flag de rollback (usar 'X' si aplica)",
        example="",
        default=""
    )
    flgDependencies: str = Field(
        description="Flag de dependencias (usar 'X' si aplica)",
        example="X",
        default=""
    )

    components: List[Component] = Field(
        default_factory=list,
        description="Lista de componentes a desplegar",
        example=[
            {
                "type": "Pipeline",
                "route": "pipeline-pagos",
                "repository": "repo-pagos",
                "pullRequest": "https://git/mi-org/pr/88",
                "observations": "Actualiza dependencias"
            },
            {
                "type": "Legacy",
                "route": "",
                "repository": "TRC",
                "pullRequest": "https://git/mi-org/pr/89",
                "observations": "Actualiza dependencias de proyecto antiguo"
            }
        ]
    )
    scripts: Optional[List[Script]] = []
    rollbackScripts: Optional[List[RollbackScript]] = []
    steps: Optional[List[Step]] = []
    rollbackPlans: Optional[List[RollbackPlan]] = []
    verifications: Optional[List[Verification]] = []
    approvers: Optional[List[Approver]] = []

