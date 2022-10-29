from pydantic import BaseModel

class AccountSchemas(BaseModel):
    fullname: str
    username: str
    pwd: str
    
class LoginSchemas(BaseModel):
    username: str
    pwd: str