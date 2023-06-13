from reactpy import html, component, hooks


def increment(last_count):
    return last_count + 1


def decrement(last_count):
    return last_count - 1


initial_count = 0


@component
def Counter(disabled: bool = False, **props):
    count, set_count = hooks.use_state(initial_count)

    classname = {
        "container": "relative",
        "select": "px-2 bg-red-300",
        "icon": "absolute inset-y-0 right-0 flex items-center px-2 pointer-events-none",
    }

    return html.div(
        f"Count: {count}",
        html.div(
            html.button(
                {
                    "class": classname["select"],
                    "disabled": disabled,
                    "on_click": lambda event: set_count(initial_count)
                },
                "Reset"
            ),
        ),
        html.button(
            {"on_click": lambda event: set_count(increment)}, "+"),
        html.button({"on_click": lambda event: set_count(decrement)}, "-"),
        # html.link({}, "https://qiita.com/kzy83/items/4c6ef4e68b3755d7549f")
    )
