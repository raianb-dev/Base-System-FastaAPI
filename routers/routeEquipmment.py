from enum import Enum
from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session
from encrypt.jwt import ACCESS_SECURITY, JWTAUTH

from views.serializer.to_json import build_toJson
from views.equipmmentSchemas import equipmmentSchema
from dbconnection.connection import get_db
from orm import ormEquipmment

class Tags(Enum):
    Order = "equipmment"

router = APIRouter()

@router.post('/v1/api/Equipmment/', response_model=equipmmentSchema, tags=[Tags.Order])
async def post_equipmment(Order: equipmmentSchema, db: Session = Depends(get_db)):
    data, status = ormEquipmment.add_Equipmment(db, Order)
    return build_toJson(status=status, content=data)

@router.get('/v1/api/Equipmment/', response_model=equipmmentSchema, tags=[Tags.Order])
async def get_equipmment(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    data, status = ormEquipmment.get_Equipmment(db, skip, limit)
    return build_toJson(status=status, content=data)

@router.get('/v1/api/Equipmment/{id}',response_model=equipmmentSchema, tags=[Tags.Order])
async def get_byid(id: str, db: Session = Depends(get_db)):
    data, msg,  status = ormEquipmment.get_byid_Equipmment(db, id)
    return build_toJson(status=status, content=data, alert=msg)

@router.put('/v1/api/Equipmment/{id}', response_model=equipmmentSchema, tags=[Tags.Order])
async def put_equipmment(id: str, Order: equipmmentSchema, db: Session = Depends(get_db)):
    data, status = ormEquipmment.update_Equipmment(db, id, Order)
    return build_toJson(status=status, content=data)
    
@router.delete('/v1/api/Equipmment/{id}', response_model=equipmmentSchema, tags=[Tags.Order])
async def delete_equipmment(id: str, db: Session = Depends(get_db)):
    data, status = ormEquipmment.delete_Equipmment(db, id)
    return build_toJson(status=status, content=data)