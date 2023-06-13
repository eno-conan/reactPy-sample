
from reactpy import html, component, hooks
from reactpy_router import link
from src.components import Button
from src.components.layout import Layout


@component
def Home():
    my_params = "reactpy-handson"
    children = html.div(
        {
            "class": "text-center",
        },
        html.h1(
            {
                "class": "text-4xl font-semibold my-2",
            },
            "Home"
        ),
        html.div(
            html.div(
                {
                    "class": "text-xl my-2 mx-10 text-gray-500",
                },
                "ReactPy is a library for building user interfaces in Python without Javascript. ReactPy interfaces are made from components that look and behave similar to those found in ReactJS. Designed with simplicity in mind, ReactPy can be used by those without web development experience while also being powerful enough to grow with your ambitions."
            ),
            html.div(
                {
                    "class": "text-xl my-2 hover:underline hover:text-blue-600",
                },
                html.a(
                    {"href": "https://github.com/reactive-python/reactpy",
                        "target": "_blank"},
                    "Click here! Check More Information",
                ),
            )
        ),
        html.h3(
            {
                "class": "text-2xl font-bold my-4",
            },
            "Contents"
        ),
        html.div(
            {
                "class": "my-4",
            },
            Button(
                link("Qiita Article Page", to="/data"), variant="primary"
            ),
        ),
        html.div(
            {
                "class": "my-4",
            },
            Button(
                link("Data Table ", to="/table"),
                variant="primary"),
        ),
        html.div(
            {
                "class": "my-4",
            },
            Button(
                link("My Page", to="/detail/{}".format(my_params)),
                variant="primary"),
        ),
    )
    return Layout(children)
