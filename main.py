from fastapi import FastAPI
from container import Container
from ddd.presentation.api import endpoints


container = Container()
app = FastAPI()
app.container = container
app.include_router(endpoints.router)



