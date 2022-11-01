from pydantic import BaseModel

class OrdersSchemas(BaseModel):
    typeId: int
    typeserviceId: int
    equipammentId: str
    levelGravitId: int
    description: str
    priority: int
    
class OrdersSelectSchemas(BaseModel):
    number: str
    createdAt: str
    