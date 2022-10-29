from enum import Enum
from fastapi import APIRouter, Depends, Security
from encrypt.jwt import ACCESS_SECURITY, JWTAUTH

from views.serializer.to_json import build_toJson

class Tags(Enum):
    account = "account"

router = APIRouter

