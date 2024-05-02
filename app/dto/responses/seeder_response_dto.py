from pydantic import BaseModel

class SeederResponsetDTO(BaseModel):
    message: str
    