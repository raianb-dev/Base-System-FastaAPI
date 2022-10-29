from encrypt.jwt import  ACCESS_SECURITY, JWTAUTH
from fastapi import APIRouter, Depends, Security
from sqlalchemy.orm import Session
from enum import Enum



from views.serializer.to_json import build_toJson
from dbconnection.connection import get_db
from views.accountSchemas import AccountSchemas, LoginSchemas
from orm import ormAccount, ormLogin


router = APIRouter()


class Tags(Enum):
    account = "account"


@router.post('/v1/api/account', response_model= AccountSchemas, tags=[Tags.account])
async def post_account(Account: AccountSchemas, db: Session = Depends(get_db)):
    data, status = ormAccount.add_account(db, Account)
    return build_toJson(status=status, content=data)


@router.get('/v1/api/account', response_model= AccountSchemas, tags=[Tags.account])
async def get_account(skip: int = 0, limit: int = 20, db: Session = Depends(get_db), token: JWTAUTH = Security(ACCESS_SECURITY)):
    data, status = ormAccount.get_account(db, skip, limit)
    return build_toJson(status=status, content=data)


@router.get('/v1/api/account/{id}', response_model=AccountSchemas, tags=[Tags.account] )
async def getby_id(id: str, db: Session = Depends(get_db), credentials: JWTAUTH = Security(ACCESS_SECURITY)):
    data, status = ormAccount.get_byid_account(db, id)
    return build_toJson(status=status, content=data)


@router.put('/v1/api/account/{id}',
        response_model=AccountSchemas,
        tags=[Tags.account]
        )
async def put_account(id: str, account: AccountSchemas, db: Session = Depends(get_db), credentials: JWTAUTH = Security(ACCESS_SECURITY)):
    data, status = ormAccount.update_account(db, id, account)
    return build_toJson(status=status, content=data)


@router.delete('/v1/api/account/{id}',
                response_model=AccountSchemas,
                tags=[Tags.account]
            )
async def delete_account(id: str, db: Session = Depends(get_db), credentials: JWTAUTH = Security(ACCESS_SECURITY) ):
    data, status = ormAccount.delete_account(db, id)
    return build_toJson(status=status, content=data)

@router.post('/v1/api/account/login',
            response_model=LoginSchemas,
            tags=[Tags.account]     
        )
async def login(login: LoginSchemas, db: Session = Depends(get_db)):
    username = str(login.username)
    pwd = str(login.pwd)
    data, status = ormLogin.login(db, username, pwd)
    if status == 200:
        return build_toJson(status=status, content=data, token=ACCESS_SECURITY.create_access_token({'username':username}))
    else:
        return build_toJson(status=status, content=data)
