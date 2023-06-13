from fastapi import FastAPI
from uvicorn import run
from reactpy import component, html
from reactpy.backend.fastapi import configure, Options
from reactpy_router import route, simple

from src.config import head
from src.pages import Home, Detail, Data, FilterableList, Error




@component
def my_router():
    return simple.router(
        route("/", Home()),
        route("/data", Data()),
        route("/table", FilterableList()),
        route("/detail/{names}", Detail()),
        route("/er", Error()),
        route("*", html.h1("Not Found"))
    )


app = FastAPI()
configure(
    app,
    my_router,
    Options(head=head.create_head(tailwind_config={})),
)

if __name__ == "__main__":
    run(app)
