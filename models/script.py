from pydantic import BaseModel, Field
from .enums import ScriptType

class Script(BaseModel):
    order: int
    name: str
    database: str
    schema_name: str = Field(alias="schema")
    type: ScriptType
    description: str
    validator: str
