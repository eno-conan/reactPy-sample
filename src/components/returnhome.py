from reactpy import html, component
from reactpy_router import link


@component
def ReturnHomeButton():
    return html.button(
        {
            "class": "bg-lime-300 border border-transparent font-medium rounded px-2 mb-4",
        },
        link("<< Return home", to="/"),
    )
