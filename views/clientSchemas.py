from pydantic import BaseModel


class clientSchemas(BaseModel):
    fullname: str
    cpf: str
    datanasc: str
    tel: int
    email: str
    address: str
    uf: str
    city: str