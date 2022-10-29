from sqlalchemy.orm import Session
import uuid


from models.modelsAccount import Account
from views.accountSchemas import AccountSchemas


def add_account(db: Session, account: AccountSchemas):
    uuidOne = str(uuid.uuid4())
    
    add_account = Account(
            id = uuidOne,
            fullname = account.fullname,
            username = account.username,
            pwd = account.pwd
        )
    db.add(add_account)
    db.commit()
    msg = {
            'id': add_account.id,
            'fullname': add_account.fullname
        }
    return msg, 200

'''msg = 'Account not add'
        return msg, 400'''
    
def get_account(db: Session, skip: int = 0, limit: int = 20):
    try:
        query = db.query(Account).offset(skip).limit(limit).all()
        data = [Account.getAccount() for Account in query]
        return data, 200
    except:
        msg = 'Accounts not foud'
        return msg, 400

def get_byid_account(db: Session, id: str):
    try:
        query = db.query(Account).filter(Account.id == id).one()
        data = [Account.getById() for Account in query]
        
        if(data):
            return data, 200
        else:
            msg = 'Account not found or id invalid'
            return msg, 400
    except: 
        msg = 'Error'
        return msg, 403

def update_account(db: Session, id: str, account: AccountSchemas):
    query = db.query(Account).filter(Account.id == id).one()
    try:
        query.fullname = account.fullname
        query.username = account.username
        db.merge(query)
        db.commit()
        msg = 'Updated Account success'
        return msg, 200
    except:
        msg = 'Account not updated'
        return msg, 400

def delete_account(db: Session, id: str):
    try:
        query = db.query(Account).filter(Account.id == id).one()
        db.delete(query)
        db.commit()
        msg = 'Account deleted success'
        return msg, 200
    except:
        msg = 'Account not deleted'
        return msg, 400