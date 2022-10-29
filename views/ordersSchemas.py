from pydantic import BaseModel

class OrdersSchemas(BaseModel):
    typeId: str
    typeserviceId: str
    equipammentId: str
    levelGravitId: str
    description: str
    priority: str
    
class OrdersSelectSchemas(BaseModel):
    number: str
    createdAt: str
    