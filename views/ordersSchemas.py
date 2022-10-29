from pydantic import BaseModel

class OrdersSchemas(BaseModel):
    number: str
    typeId: str
    typeserviceId: str
    createdAt: str
    equipammentId: str
    levelGravitId: str
    description: str
    priority: str