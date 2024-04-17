from fastapi import FastAPI
from routers import routeAccount, routerClient, \
    routeOrders, routeResident

api = FastAPI(  title='Dominio',
                version='0.1',
                description='Documentação Swagger',
                debug=True,
                docs_url='/'
        
           )

api.include_router(routeAccount.router)
api.include_router(routerClient.router)
api.include_router(routeOrders.router)
api.include_router(routeResident.router)
