from reactpy_router.core import use_params
from reactpy import component, html
from src.components.layout import Layout
from src.components.returnhome import ReturnHomeButton


@component
def Detail():
    names = set(use_params()['names'].split("-"))
    result_names = ' '.join(names)
    children = html.div(
        ReturnHomeButton(),
        html.div(
            {
                "class": "text-center",
            },
            html.h1(
                {
                    "class": "text-4xl font-serif my-4 text-green-500",
                },
                f'details page you param is {result_names}'),
                html.div(
                    {
                    "class": "text-2xl font-bold my-4",
                },
                    "Creating... My Page"
                )
        )
    )
    return Layout(children)
