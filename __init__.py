from fastapi import FastAPI
from routers.routeAccount import router as routeAccountRouter
from routers.routerClient import router as routerClientRouter
from routers.routeOrders import router as routeOrdersRouter
from routers.routeResident import router as routeResidentRouter
from routers.routeProxy import router as routeProxyRouter

app = FastAPI(
    title='Dominio',
    version='0.1',
    description='Documentação Swagger',
    debug=True,
)

app.include_router(routeAccountRouter)
app.include_router(routerClientRouter)
app.include_router(routeOrdersRouter)
app.include_router(routeResidentRouter)
app.include_router(routeProxyRouter)


