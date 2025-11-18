from pydantic import BaseModel, Field
from .enums import ScriptType

class Script(BaseModel):
    order: int
    name: str
    database: str
    schema_name: str = Field(alias="schema")
    type: ScriptType = Field(
        description="Tipo de script (DML: Modificacion de estructura,DDL: Modificacion de data)",
        example="DML"
    )
    description: str
    validator: str
