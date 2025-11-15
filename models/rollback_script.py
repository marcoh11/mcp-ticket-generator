from pydantic import BaseModel

class RollbackScript(BaseModel):
    order: int
    name: str
    database: str
    schema: str
    description: str
