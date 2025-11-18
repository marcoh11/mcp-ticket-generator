from pydantic import BaseModel,Field
from typing import Optional
from .enums import ComponentType

class Component(BaseModel):
    type: ComponentType = Field(
        description="Tipo componentes a desplegar (Pipeline,Legacy)",
        example="Pipeline"
    )
    route: Optional[str] = None
    repository: str
    pullRequest: str
    observations: Optional[str] = None
