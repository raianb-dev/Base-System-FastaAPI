from pydantic import BaseModel

class AccountSchemas(BaseModel):
    id: str
    fullname: str
    username: str