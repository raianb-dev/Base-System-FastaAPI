from encrypt.jwt import ACCESS_SECURITY, JWTAUTH
from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session
from enum import Enum


from views.serializer.to_json import build_toJson
from views.clientSchemas import clientSchemas
from dbconnection.connection import get_db
from orm import ormClient

# token: JWTAUTH = Security(ACCESS_SECURITY)
router = APIRouter()

class Tags(Enum):
    client = "Gerenciamento de Cliente"
    
@router.post('/v1/api/client', response_model=clientSchemas, tags=[Tags.client])
async def post_client(Client: clientSchemas, db: Session = Depends(get_db),):
    data, status = ormClient.add_client(db, Client)
    return build_toJson(status=status, content=data)

@router.get('/v1/api/client', response_model=clientSchemas, tags=[Tags.client])
async def get_client(name: str = None,skip: int = 0, limit: int = 20,db: Session = Depends(get_db),):
    data, status = ormClient.get_client(db, skip, limit, name)
    return build_toJson(status=status, content=data)

@router.get('/v1/api/client/{id}', response_model=clientSchemas, tags=[Tags.client])
async def get_byid(id: str, db: Session = Depends(get_db),):
    data, status = ormClient.get_byid_client(db, id)
    return build_toJson(status=status, content=data)

@router.put('/v1/api/client/{id}', response_model=clientSchemas, tags=[Tags.client])
async def put_client(id: str, client: clientSchemas, db: Session = Depends(get_db),):
    data, status = ormClient.put_client(db, client, id)
    return build_toJson(status=status, content=data)

@router.delete('/v1/api/client/{id}', response_model=clientSchemas, tags=[Tags.client])
async def delete_client(id: str, db: Session = Depends(get_db), ):
    data, status = ormClient.delete_client(db, id)
    return build_toJson(status=status, content=data)

