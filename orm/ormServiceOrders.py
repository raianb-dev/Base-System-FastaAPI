import json
import random
from sqlalchemy.orm import Session
import uuid

from models.modelsServiceOrders import Equipmment, ServiceOrdres
from views.ordersSchemas import OrdersSchemas


def add_Order(db: Session, serviceOrders: OrdersSchemas):
   uuidOne = str(uuid.uuid4())
   try:
       uuidOne = str(uuid.uuid4())
       add_os = ServiceOrdres(
           id = uuidOne,
           number = int(random.uniform(10000, 99999)),
           typeid = serviceOrders.typeId,
           typeserviceid = serviceOrders.typeserviceId,
           equipmmentid = serviceOrders.equipammentId,
           levelgravitid = serviceOrders.levelGravitId,
           description = serviceOrders.description,
           priority = serviceOrders.priority
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
    
    query = db.query(ServiceOrdres).filter(ServiceOrdres.id == id)
    equipmmentId, equipmmentName = list(db.query(Equipmment.id, Equipmment.name).select_from(ServiceOrdres).where(ServiceOrdres.equipmmentid == Equipmment.id))
    data = [ServiceOrdres.Get_byId(equipmmentId[0], equipmmentName[1]) for ServiceOrdres in query]
    
    if(data):  
        return data, 200 
    else:
        msg = 'OS not found or id invalid'
        return msg
    
def update(db: Session, id: str, Order: OrdersSchemas):
    query = db.query(ServiceOrdres).filter(ServiceOrdres.id == id)
  
    query.typeId = Order.typeId,
    query.typeserviceId = Order.typeserviceId,
    query.equipmment = Order.equipammentId,
    query.levelGravitId = Order.levelGravitId,
    query.description = Order.description,
    query.priority = Order.priority
        
    db.merge(query)
    db.commit()
    msg = 'updated order success'
    return msg, 200

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