from pydantic import BaseModel

class residentSchemas(BaseModel):

    document: str
    fullname : str
    apto : str
    block : str
    phone : str
    email : str
    client_id : str
    
class residenteSchemasPut(BaseModel):
    fullname : str
    document: str
    apto: str
    block: str
    email : str
    phone: str
    