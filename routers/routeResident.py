from encrypt.jwt import ACCESS_SECURITY, JWTAUTH
from fastapi import APIRouter, Depends, Security, Query
from sqlalchemy.orm import Session
from enum import Enum


from views.serializer.to_json import build_toJson
from dbconnection.connection import get_db
from views.residentSchemas import residentSchemas, residenteSchemasPut
from orm import ormResident

router = APIRouter()

class Tags(Enum):
    enum_resident = "Gerenciamento Propietários"
    
@router.post('/v1/api/resident', response_model=residentSchemas, tags=[Tags.enum_resident])
async def post_resident(Resident: residentSchemas, db: Session = Depends(get_db)):
    status, data = ormResident.add_resident(db, Resident)
    return build_toJson(status, data)

@router.get('/v1/api/resident', response_model=residentSchemas, tags=[Tags.enum_resident])
async def get_residents(clientId:str, skip: int = 0, limit: int = 20,db: Session = Depends(get_db)):
    status, data = await ormResident.get_resident(db, clientId, skip, limit)  # Sem await aqui
    return build_toJson(status, data)

@router.get('/v1/api/resident/{id}', response_model=residentSchemas, tags=[Tags.enum_resident])
async def getbyid_resident(id:str, db: Session = Depends(get_db)):
    status, data =  ormResident.getBy_id(db,id,)
    return build_toJson(status, data)

@router.put("/v1/api/resident/{id}", response_model=residenteSchemasPut, tags=[Tags.enum_resident])
async def put_resident(id: str, resident: residentSchemas, db:Session = Depends(get_db)):
    status, data = ormResident.put_resident(db, resident, id)
    return build_toJson(status, data)

@router.delete('/v1/api/resident/{id}', response_model=residentSchemas, tags=[Tags.enum_resident])
async def delete_residents(id:str, db:Session = Depends(get_db)):
    status, data = ormResident.delete(db, id)
    return build_toJson(status, data)