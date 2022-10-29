from models.modelsAccount import Account
from sqlalchemy.orm import Session


def login(db: Session, username: str, pwd: str):
    try:
        q_username = db.query(Account).filter(Account.username == username)
        query = [Account.getById() for Account in q_username]
        q_pwd = query[0]['pwd']
        q_username = query[0]['username']

        if (query) and q_pwd == pwd and q_username == username :
            return 'Success login', 200
        else:
            return 'Username or password incorrect', 400
    except:
        msg = 'Username or password incorrect'
        return msg, 403

    