from models.modelsClient import Resident
from sqlalchemy.orm import Session
from views.residentSchemas import residentSchemas

def add_resident(db: Session, resident: residentSchemas):
    try:
        add = Resident(
            fullname = resident.fullname,
            document = resident.document,
            apto = resident.apto,
            block = resident.block,
            phone = resident.phone,
            email = resident.email,
            client_id = resident.client_id
        )
        db.add(add)
        db.commit()
        msg = 'Resident added sucessfull'
        return 200, msg
    except:
        msg = 'Resident is not added'
        return 400, msg

def put_resident(db: Session, resident: residentSchemas, id: str):
    try:
        query = db.query(Resident).filter(Resident.id == id).one()
        query.document = resident.document
        query.fullname = resident.fullname
        query.apto = resident.apto
        query.block = resident.block
        query.phone = resident.phone
        query.email = resident.email
        
        db.merge(query)
        db.commit()
        msg = 'Residente updated successfull'
        return 200, msg
    except:
        msg = 'Residente is not updated'
        return 400, msg

async def get_resident(db: Session, clientId: str, skip: int = 0, limit: int = 20):
    try:
        query = db.query(Resident).filter(Resident.client_id == clientId).offset(skip).limit(limit).all()
        data = [Resident.get() for Resident in query]
        print(clientId, query)
        return 200, data
    except:
        msg = 'Resident not found'
        return 400, msg
    
async def get_resident_apto_block(db: Session, apto: str, block: str):
    query = db.query(Resident).filter(Resident.apto == apto and Resident.block == block)
    data = [Resident.getby_id() for Resident in query]
    return 200, data
        
def getBy_id(db:Session,id: str):
    try:
        query = db.query(Resident).filter(Resident.id == id)
        data = [Resident.getby_id() for Resident in query]
        return 200, data
    except:
        msg = 'Not found'
        return 400, msg

def delete(db: Session, id: str):
    try:
        query = db.query(Resident).filter(Resident.id == id)
        db.delete(query)
        db.commit()
        msg = 'Deleted successfull'
        return 200, msg
    except:
        msg = 'Is not deleted'
        return 400, msg