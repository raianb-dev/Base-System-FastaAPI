from models.modelsStatus import Statuses
from views.statusesSchemas import StatusesSchemas


from sqlalchemy.orm import Session

def add_status(db: Session, status: StatusesSchemas):

    add = Statuses(
        id = status.id,
        name = status.name, 
        subprocess = status.subprocess
    )
    db.add(add)
    db.commit()
    content = {
        'id': add.id,
        'name': add.name
    }
    return content, 200

def get_status(db: Session, skip: int = 0, limit: int = 20):
    query = db.query(Statuses).offset(skip).limit(limit).all()
    data = [Statuses.get() for Statuses in query]
    if (data):
        return data, 200
    return None, 400


def get_byId(db: Session, id: str):
    query = db.query(Statuses).filter(id == Statuses.id)
    data = [Statuses.get() for Statuses in query]
    if (data):
        return data, 200
    return None, 400

def put_status(db: Session, status: StatusesSchemas, id: int):
    query = db.query(Statuses).filter(id == Statuses.id).one()
    query.name = status.name
    
    db.merge(query)
    db.commit()
    msg = 'updated suceess'
    return msg, 200

def delete_status(db: Session, id: int):
    query = db.query(Statuses).filter(id == id).one()
    db.delete(query)
    db.commit()
    msg = 'deleted success'
    return msg, 200
    