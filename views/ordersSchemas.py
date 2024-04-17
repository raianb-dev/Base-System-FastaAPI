from pydantic import BaseModel, HttpUrl
from typing import Optional


    
class orderSchemas(BaseModel):
    
    clientId: str
    barcode : str
    apto : str
    block : str

    
class orderSchemas_put(BaseModel):
    apto: str

class ordersImage(BaseModel):
    orderId: str
    base64: str
    
