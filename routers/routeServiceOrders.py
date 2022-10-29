from enum import Enum
from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session
from encrypt.jwt import ACCESS_SECURITY, JWTAUTH

from views.serializer.to_json import build_toJson
from views.ordersSchemas import OrdersSchemas, OrdersSelectSchemas
from dbconnection.connection import get_db
from orm import ormServiceOrders

class Tags(Enum):
    Order = "service_orders"

router = APIRouter()

@router.post('/v1/api/serviceOrders/', response_model=OrdersSchemas, tags=[Tags.Order])
async def post_order(Order: OrdersSchemas, db: Session = Depends(get_db), token: JWTAUTH = Security(ACCESS_SECURITY)):
    data, status = ormServiceOrders.add_Order(db, Order)
    return build_toJson(status=status, content=data)

@router.get('/v1/api/serviceOrders/', response_model=OrdersSelectSchemas, tags=[Tags.Order])
async def get_order(skip: int = 0, limit: int = 20, db: Session = Depends(get_db), token: JWTAUTH = Security(ACCESS_SECURITY)):
    data, status = ormServiceOrders.get_Order(db, skip, limit)
    return build_toJson(status=status, content=data)

@router.get('/v1/api/serviceOrders/{id}',response_model=OrdersSchemas, tags=[Tags.Order])
async def get_byid_order(id: str, db: Session = Depends(get_db), token: JWTAUTH = Security(ACCESS_SECURITY)):
    data, status = ormServiceOrders.get_byid(db, id)
    return build_toJson(status=status, content=data)

@router.put('/v1/api/serviceOrders/{id}', response_model=OrdersSchemas, tags=[Tags.Order])
async def put_order(id: str, Order: OrdersSchemas, db: Session = Depends(get_db), token: JWTAUTH = Security(ACCESS_SECURITY)):
    data, status = ormServiceOrders.update(db, id, Order)
    build_toJson(status=status, content=data)
    
@router.delete('/v1/api/serviceOrder/{id}', response_model=OrdersSchemas, tags=[Tags.Order])
async def delete_order(id: str, db: Session = Depends(get_db), token: JWTAUTH = Security(ACCESS_SECURITY)):
    data, status = ormServiceOrders.delete_order(db, id)
    build_toJson(status=status, content=data)