from pydantic import BaseModel
from .enums import ScriptType

class Script(BaseModel):
    order: int
    name: str
    database: str
    schema: str
    type: ScriptType
    description: str
    validator: str
