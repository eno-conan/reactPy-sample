from reactpy import component, html
from reactpy.core.types import VdomChildren


@component
def Layout(children: VdomChildren):

    return html.main(
        html.div(
            {
                "class": "bg-gray-300 min-h-screen dark:bg-gray-900 dark:text-white",
            },
            html.div(
                {
                    "class": "container mx-auto p-2",
                },
                html.div(
                    {"class": "flex justify-center items-center my-8"},
                    html.img(
                        {
                            "src": "https://reactpy.dev/docs/_static/reactpy-logo-landscape.svg",
                            # "src": "https://avatars.githubusercontent.com/u/106191177?s=200&v=4",
                            "style": {"width": "35%"},
                            "alt": "reactPy",
                        }
                    ),
                ),
                children,
            ),
        ),
    )
