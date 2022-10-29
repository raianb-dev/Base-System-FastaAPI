from fastapi import FastAPI
from routers import routeAccount

api = FastAPI(title='Commercial API', version='0.1')

api.include_router(routeAccount.router)
