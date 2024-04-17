from models.modelsClient import Client
from views.clientSchemas import clientSchemas


from sqlalchemy.orm import Session
import uuid


def add_client(db: Session, client: clientSchemas):
    uuidOne = str(uuid.uuid4())
    add = Client(
        id = uuidOne,
        fullname = client.fullname,
        cpf = client.cpf,
        datanasc = client.datanasc,
        tel = client.tel,
        email = client.email,
        address = client.address,
        uf = client.uf,
        city = client.city
    )
    db.add(add)
    db.commit()
    content = {
        "id": add.id,
        "name": add.fullname
    }
    return content, 200

def get_client(db: Session, skip: int = 0, limit: int = 20, name: str = None):
    query = db.query(Client).offset(skip).limit(limit).all()
    if(name):
        query = db.query(Client).filter(Client.fullname.like(f'%{name}%'))
    data = [Client.get() for Client in query]
    return data, 200

def get_byid_client(db: Session, id: str):
    query = db.query(Client).filter(id == id)
    data = [Client.get_byId() for Client in query]
    return data, 200

def put_client(db: Session, client: clientSchemas, id: str):
    query = db.query(Client).filter(id == id).one()
    
    query.fullname = client.fullname
    query.cpf = client.cpf
    query.datanasc = client.datanasc
    query.tel = client.tel
    query.email = client.email
    query.address = client.address
    query.uf = client.uf
    query.city = client.city
    
    db.merge(query)
    db.commit()
    
    msg = 'Updated success'
    return msg, 200
    
def delete_client(db: Session, id: str):
    query = db.query(Client).filter(Client.id == id).one()
    db.delete(query)
    db.commit()
    msg = 'deleted success'
    return msg, 200