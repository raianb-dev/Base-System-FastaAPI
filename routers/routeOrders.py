from encrypt.jwt import ACCESS_SECURITY, JWTAUTH
from fastapi import APIRouter, Depends, Security, Query, File, UploadFile
from sqlalchemy.orm import Session
from enum import Enum


from views.serializer.to_json import build_toJson
from dbconnection.connection import get_db
from views.ordersSchemas import orderSchemas, orderSchemas_put, ordersImage
from storage.gcloud import upload_image_to_gcs

from orm import ormOrders
from orm import ormResident
from orm.apps import notfy

notfy = notfy.send_email

router = APIRouter()
# token: JWTAUTH = Security(ACCESS_SECURITY)
class Tags(Enum):
    enum_orders = "Gerenciamento de Encomendas"
    
@router.post('/v1/api/order', response_model=orderSchemas, tags=[Tags.enum_orders])
async def post_order( orders: orderSchemas, db: Session = Depends(get_db),):
    
    # notification = notfy(orders.barcode, orders.block, orders.apto, orders.clientId, orders.image)

    data, status = await ormOrders.add_order(db,orders)
    return build_toJson(status, data)

@router.post('/v1/api/order/image', response_model=ordersImage, tags=[Tags.enum_orders])
async def post_image(image: ordersImage, db: Session = Depends(get_db)):
    data, status  = await ormOrders.get_byid_orders(db, image.orderId)
    url_image = await upload_image_to_gcs(image.base64, data[0]['barcode'])
    notification = notfy(data[0]['barcode'], data[0]['block'], data[0]['apto'], data[0]['clientId'], url_image)
    return build_toJson(status, notification)

@router.get("/v1/api/orders", response_model=orderSchemas, tags=[Tags.enum_orders])
async def get_order(clientId:str, skip: int = 0, limit: int = 20, db: Session = Depends(get_db),):
    data, status = await ormOrders.get_orders(db, clientId, skip, limit)
    return build_toJson(status, data) 

@router.get("/v1/api/order/{id}", response_model=orderSchemas, tags=[Tags.enum_orders])
async def get_byId_order(id:str, db:Session = Depends(get_db), ):
    data, status  = await ormOrders.get_byid_orders(db, id)
    return build_toJson(status, data)

@router.put("/v1/api/order/{id}", response_model=orderSchemas_put, tags=[Tags.enum_orders])
async def put_order(id:str, orders: orderSchemas_put, db: Session = Depends(get_db), ):
    data, status = await ormOrders.put_orders(db, orders, id)
    return build_toJson(status, data)

@router.delete("/v1/api/order/{id}", response_model=orderSchemas, tags=[Tags.enum_orders])
async def delete_order(id:str, db:Session = Depends(get_db), ):
    data, status = await ormOrders.delete_orders(db, id)
    return build_toJson(status, data)