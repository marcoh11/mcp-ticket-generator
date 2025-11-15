from pydantic import BaseModel

class RollbackPlan(BaseModel):
    context: str
    action: str
    responsable: str
    time: str
