from pydantic import BaseModel

class StatusesSchemas(BaseModel):
    id: int
    name: str    
    subprocess: str