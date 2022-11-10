from fastapi import FastAPI
from routers import routeAccount, routeServiceOrders, routeServiceOrders,\
                    routeEquipmment,routerClient,routeNotefiscal, routeStatuses\


api = FastAPI(title='Commercial API', version='0.1')

api.include_router(routeAccount.router)
api.include_router(routeServiceOrders.router)
api.include_router(routeEquipmment.router)
api.include_router(routerClient.router)
api.include_router(routeNotefiscal.router)
api.include_router(routeStatuses.router)
