from views.defaultSchemas import DefaultSchemas
from views.serializer.to_json import build_toJson
from fastapi import APIRouter

router = APIRouter()

@router.get('/home', response_model=DefaultSchemas, tags=['Home'])
async def home():
    msg = 'Connection success. '
    return build_toJson(status=200, content=None, alert=msg)
