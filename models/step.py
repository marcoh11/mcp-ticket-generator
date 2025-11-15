from pydantic import BaseModel
from typing import Optional

class Step(BaseModel):
    order: int
    description: str
    responsable: str
    action: Optional[str] = None
    result: Optional[str] = None
