from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from enum import Enum


from views.serializer.to_json import build_toJson
from views.notefiscalSchemas import noteficalSchemas
from dbconnection.connection import get_db
from orm import ormNotefical


router = APIRouter()

class Tags(Enum):
    name = "invoice"

@router.post('/v1/api/note/', response_model=noteficalSchemas, tags=[Tags.name])
async def post(note: noteficalSchemas, db: Session = Depends(get_db)):
    data, status = ormNotefical.add_notes(db, note)
    return build_toJson(status=status, content=data)

@router.get('/v1/api/notes/', response_model=noteficalSchemas, tags=[Tags.name] )
async def get(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    data, status = ormNotefical.get_notes(db, skip, limit)
    return build_toJson(status=status, content=data)

@router.get('/v1/api/note/{id}', response_model=noteficalSchemas, tags=[Tags.name])
async def get_byid(id: str, db: Session = Depends(get_db)):
    data, status = ormNotefical.get_byId_notes(db, id)
    return build_toJson(status=status, content=data)

@router.put('/v1/api/note/{id}', response_model=noteficalSchemas, tags=[Tags.name])
async def put(note: noteficalSchemas, id: str, db: Session = Depends(get_db)):
    data, status = ormNotefical.put_notes(db, note, id)
    return build_toJson(status=status, content=data)

@router.delete('/v1/api/note/{id}', response_model=noteficalSchemas, tags=[Tags.name])
async def delete(id: str, db: Session = Depends(get_db)):
    data, status = ormNotefical.delete_notes(db, id)
    return build_toJson(status=status, content=data)

    