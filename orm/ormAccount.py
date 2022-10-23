from cmath import acos
from sqlalchemy.orm import Session
import uuid

from models.modelsAccount import Account
from views.accountSchemas import AccountSchemas

def add_account(db: Session, account: AccountSchemas):
    uuidOne = str(uuid.uuid4())
    try:
        add_account = Account(
            id = uuidOne,
            fullname = account.fullname,
            username = account.username
        )
        db.add(add_account)
        db.commit()
        return{
            'id': add_account.id,
            'fullname': add_account.fullname
        }
    except:
        msg = 'Account not add.'
        return msg
    
def get_account(db: Session, skip: int = 0, limit: int = 20):
    try:
        query = db.query(Account).offset(skip).limit(limit).all()
        data = [Account.getAccount() for Account in query]
        return data
    except:
        msg = 'Accounts not foud.'
        return msg

def get_byid_account(db: Session, id: str):
    try:
        query = db.query(Account).filter(Account.id == id)
        data = [Account.getById() for Account in query]
        return data
    except: 
        msg = 'Account not found.'
        return msg

def update_account(db: Session, id: str, account: AccountSchemas):
    query = db.query(Account).filter(Account.id == id).one()
    try:
        query.fullname = account.fullname
        query.username = account.username
        db.merge(query)
        db.commit()
        msg = 'Updated Account success.'
        return msg
    except:
        msg = 'Account not updated'
        return msg

def delete_account(db: Session, id: str):
    try:
        query = db.query(Account).filter(Account.id == id).one()
        db.delete(query)
        db.commit()
        msg = 'Account deleted success.'
        return msg
    except:
        msg = 'Account not deleted.'
        return msg