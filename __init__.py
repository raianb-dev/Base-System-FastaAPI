from fastapi import FastAPI
from routers import routeAccount, routeServiceOrders, routeEquipmment

api = FastAPI(title='Commercial API', version='0.1')

api.include_router(routeAccount.router)
api.include_router(routeServiceOrders.router)
api.include_router(routeEquipmment.router)
