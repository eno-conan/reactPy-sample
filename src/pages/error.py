from reactpy import component, html, use_state, use_effect
from src.components.layout import Layout


# RuntimeError: No life cycle hook is active. Are you rendering in a layout?
# data, set_data = use_state([])

@component
def Error():
    i = 0
    def print_hello():
        print("Hello")

    if (i == 0):
        use_effect(print_hello, [])

    children = html.h1(
        "Error "
    )
    return Layout(children)
