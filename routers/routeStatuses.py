from fastapi import APIRouter, Depends
from enum import Enum
from sqlalchemy.orm import Session
from dbconnection.connection import get_db

from views.statusesSchemas import StatusesSchemas
from views.serializer.to_json import build_toJson
from orm import ormStatuses

class Tags(Enum):
    name = "statuses"
    
router = APIRouter()

@router.post("/v1/api/status/", response_model=StatusesSchemas, tags=[Tags.name])
async def status(statuses: StatusesSchemas, db: Session = Depends(get_db)):
    data, status = ormStatuses.add_status(db, statuses)
    return build_toJson(status=status, content=data)

@router.get("/v1/api/status/", response_model=StatusesSchemas, tags=[Tags.name])
async def status_get(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    data, status = ormStatuses.get_status(db, skip, limit)
    return build_toJson(status=status, content=data)

@router.get("/v1/api/status/{id}", response_model=StatusesSchemas, tags=[Tags.name])
async def status_getby_id(id: int, db: Session = Depends(get_db)):
    data, status = ormStatuses.get_byId(db, id)
    return build_toJson(status=status, content=data)

@router.put("/v1/api/status/{id}", response_model=StatusesSchemas, tags=[Tags.name])
async def status_put(id: int, statuses: StatusesSchemas, db: Session = Depends(get_db)):
    data, status = ormStatuses.put_status(db, statuses, id)
    return build_toJson(status=status, content=data)

@router.delete("/v1/api/status/{id}", tags=[Tags.name])
async def status_delete(id: int, db: Session = Depends(get_db)):
    data, status = ormStatuses.delete_status(db, id)
    return build_toJson(status=status, content=data)




    