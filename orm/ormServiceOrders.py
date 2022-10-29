from sqlalchemy.orm import Session
import uuid

from models.modelsServiceOrders import ServiceOrdres
from views.ordersSchemas import OrdersSchemas


def add_Order(db: Session, ServiceOrders: OrdersSchemas):
   uuidOne = str(uuid.uuid4())
   try:
       add_os = ServiceOrders(
           id = uuidOne,
           number = ServiceOrders.number,
           typeId = ServiceOrders.typeId,
           typeserviceId = ServiceOrders.typeserviceId,
           createdAt = None,
           equipammentId = ServiceOrders.equipammentId,
           levelGravitId = ServiceOrders.levelGravitId,
           description = ServiceOrders.description,
           priority = ServiceOrders.priority
       )
       db.add(add_os)
       db.commit()
       msg = {
           'id': add_os.id,
           'number': add_os.number
       }
       return msg, 200
   except:     
        msg = 'OS not added'
        return msg, 400
      
def get_Order(db: Session, skip: int = 0, limit: int = 20):
    try:
        query = db.query(ServiceOrdres).offset(skip).limit(limit).all()
        data = [ServiceOrdres.Get_Orders() for ServiceOrdres in query]
        return data, 200
    except:
        msg = 'OS not found'
        return msg, 400
    
def get_byid(db: Session, id: str):
    try:
        query = db.query(ServiceOrdres).filter(ServiceOrdres.id == id)
        data = [ServiceOrdres.Get_byId() for ServiceOrdres in query]
        if(data):   
            return data, 200 
        else:
            msg = 'OS not found or id invalid'
            return msg, 400
    except:
        msg = 'Error'
        return msg, 403
    
def update(db: Session, id: str, Order: OrdersSchemas):
    query = db.query(ServiceOrdres).filter(ServiceOrdres.id == id).one()
    try:
        query.id = ServiceOrdres.id
        query.number = ServiceOrdres.number
        query.typeId = ServiceOrdres.typeId
        query.typeserviceId = ServiceOrdres.typeserviceId
        query.createAt = ServiceOrdres.createdAt
        query.equipammentId = ServiceOrdres.equipammentId
        query.levelGravitId = ServiceOrdres.levelGravitId
        query.description = ServiceOrdres.description
        query.priority = ServiceOrdres.priority
        db.merge(query)
        db.commit()
        msg = 'updated order success'
        return msg, 200
    except:
        msg = 'order not updated'
        return msg, 400
    
def delete_order(db: Session, id: str):
    try:
        query = db.query(ServiceOrdres).filter(ServiceOrdres.id == id).one()
        db.delete(query)
        db.commit()
        msg = 'OS deleted success'
        return msg, 200
    except:
        msg = 'OS not deleted'
        return msg, 400