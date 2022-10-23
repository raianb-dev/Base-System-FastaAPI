from fastapi import FastAPI
from views.defaultSchemas import DefaultSchemas
from views.serializer.to_json import build_toJson
from routes.homeRoute import router


api = FastAPI(title='Commercial API', version='0.1')
api.include_router(router)
