from pydantic import BaseModel

class Approver(BaseModel):
    role: str
    name: str
    date: str
