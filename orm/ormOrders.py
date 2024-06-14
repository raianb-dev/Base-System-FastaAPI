from models.modelsClient import Orders
from models.modelsNotification import Email
from views.ordersSchemas import orderSchemas
from datetime import datetime

from sqlalchemy.orm import Session
import uuid

async def add_order(db: Session, orders: orderSchemas):
    try:
        uuidOne = str(uuid.uuid4())
        add = Orders(
            id = uuidOne,
            client_id = orders.clientId,
            barcode = orders.barcode,
            date_in = str(datetime.now()),
            apto = orders.apto,
            block = orders.block,
            status = str("Recebido")
        )
        db.add(add)
        db.commit()
        
        msg = {"id":uuidOne}
        return msg, 200
    except:
        msg = "Orders is not added"
        return msg, 400

async def get_orders(db: Session, clientId: str, skip: int = 0, limit: int = 20):
    print(clientId)
    query = db.query(Orders).filter(Orders.client_id == clientId).offset(skip).limit(limit).all()
    data = [Orders.get(db) for Orders in query]
    return data, 200

async def get_byid_orders(db: Session, id: str):

    query = db.query(Orders).filter(Orders.id == id)
    data = [Orders.get_byid() for Orders in query]
    if (data):
        return data, 200
    else:
        msg = 'Order not found'
        return msg, 400

async def put_orders(db: Session, orders:orderSchemas, id: str):
    try:
        query = db.query(Orders).filter(Orders.id == id).one()
        
        query.apto = orders.apto
        query.date_out = str(datetime.now())
        query.status = str("delivered")
        db.merge(query)
        db.commit()
        
        msg = "Updated succesfull"
        return msg, 200
    except:
        msg = "Note Updated"
        return msg, 400

async def delete_orders(db: Session, id: str):
    try:
        query = db.query(Orders).filter(id == id).one()
        db.delete(query)
        db.commit()
        msg = "Deleted succesfull" 
        return msg, 200
    except:
        msg = "Is not deleted"
        return msg, 200

