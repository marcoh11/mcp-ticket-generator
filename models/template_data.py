from pydantic import BaseModel
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
    deploymentType: DeploymentType
    deploymentDate: str
    glpiTicketId: int
    deploymentName: str
    deploymentRequester: str
    deploymentDeveloper: str
    deploytmentApprover: str
    deploymentDescription: str

    components: Optional[List[Component]] = []
    scripts: Optional[List[Script]] = []
    rollbackScripts: Optional[List[RollbackScript]] = []
    steps: Optional[List[Step]] = []
    rollbackPlans: Optional[List[RollbackPlan]] = []
    verifications: Optional[List[Verification]] = []
    aprovers: Optional[List[Approver]] = []
