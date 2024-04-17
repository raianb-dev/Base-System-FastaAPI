from datetime import datetime, timedelta
import os
from passlib.context import CryptContext
from jose import jwt
from fastapi_jwt import JwtAccessBearer
from fastapi_jwt import JwtAuthorizationCredentials


pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")

JWTAUTH = JwtAuthorizationCredentials
SECRET_KEY = os.getenv('SECRET_KEY', 'asasasasasas')
ACCESS_SECURITY = JwtAccessBearer(secret_key=SECRET_KEY, auto_error=True)
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS512')
ACCESS_TOKEN_EXPIRE_HOURS = 999

def create_token_jwt() -> str:
    expire = datetime.utcnow() + timedelta(
        hours=ACCESS_TOKEN_EXPIRE_HOURS
    )
    to_encode = {"exp": expire, "sub": str()}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS512")
    return encoded_jwt

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)