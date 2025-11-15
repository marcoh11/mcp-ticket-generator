from pydantic import BaseModel
from typing import Optional
from .enums import ComponentType

class Component(BaseModel):
    type: ComponentType
    route: Optional[str] = None
    repository: str
    pullRequest: str
    observations: Optional[str] = None
