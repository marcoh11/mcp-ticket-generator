from pydantic import BaseModel

class Verification(BaseModel):
    description: str
    result: str
    responsable: str
    status: str
