from pydantic import BaseModel, Field

class RollbackScript(BaseModel):
    order: int
    name: str
    database: str
    schema_name: str = Field(alias="schema")
    description: str
