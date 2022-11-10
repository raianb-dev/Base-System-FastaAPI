import uuid
from models.modelsServiceOrders import Equipmment
from views.equipmmentSchemas import equipmmentSchema

from sqlalchemy.orm import Session

def add_Equipmment(db: Session, equipmment: equipmmentSchema):

        uuidOne = str(uuid.uuid4())
        add_Equipmment = Equipmment(
            id = uuidOne,
            name = equipmment.name
        )
        db.add(add_Equipmment)
        db.commit()
        msg = {
            'id': add_Equipmment.id,
            'name': add_Equipmment.name
        }
        return msg, 200

    
def get_Equipmment(db: Session, skip: int = 0, limit: int = 20):
    try:
        query = db.query(Equipmment).offset(skip).limit(limit).all()
        data = [Equipmment.get() for Equipmment in query]
        return data, 200
    except:
        msg = 'Equipmment not found or id invalid'
        return msg, 400

def get_byid_Equipmment(db: Session, id: str):
    try:
        query = db.query(Equipmment).filter(Equipmment.id == id)
        data = [Equipmment.getbyId() for Equipmment in query]
        
        if(data):
            return data, None, 200
        else: 
            data = [None]
            msg = 'Equipmment not founf or id invalid'
            return data, msg, 400
    except:
        msg = 'Error'
        return msg, 403
    
def update_Equipmment(db: Session, id: str, equipmment: equipmmentSchema):
    query = db.query(Equipmment).filter(Equipmment.id == id).one()
    try:
        query.name = equipmment.name
        db.merge(query)
        db.commit()
        msg = 'Updated equipmment success'
        return msg, 200
    except:
        msg = 'Equipmment not updated'
        return msg, 400
    
def delete_Equipmment(db: Session, id: str):
    try:
        query = db.query(Equipmment).filter(Equipmment.id == id).one()
        db.delete(query)
        db.commit()
        msg = 'Equipmment deleted success'
        return msg, 200
    except:
        msg = 'Equipmment not deleted'
        return msg, 400
    