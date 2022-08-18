from fastapi import FastAPI
import Container
from Container import Container
from ddd.Presentation.API import endpoints

student_helper = Container.student_service()


def create_app() -> FastAPI:
    container = Container()
    app = FastAPI()
    app.container = container
    app.include_router(endpoints.router)
    return app


app = create_app()
