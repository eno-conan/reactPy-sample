import json
from pathlib import Path

from reactpy import component, hooks, html
from src.components.layout import Layout
from src.components.returnhome import ReturnHomeButton

HERE = Path(__file__)
DATA_PATH = HERE.parent / "data.json"
food_data = json.loads(DATA_PATH.read_text())


@component
def Search(value, set_value):
    def handle_change(event):
        set_value(event["target"]["value"])

    # 以下のようにプロパティ一覧を定義できる
    class_name = " ".join(
        [
            "block",
            "w-1/2",
            "px-3",
            "py-1",
            "my-2",
            "text-base",
            "placeholder-gray-500",
            "border",
            "border-gray-300",
            "rounded-md",
            "shadow-sm",
            "focus:outline-none",
            "focus:ring-2",
            "focus:ring-indigo-500",
            "focus:border-indigo-500",
            "sm:text-sm",
        ]
    )
    return html._(
        html.label(
            {"class": "text-4xl text-green-500 font-serif"},
            "Search by Food Name",
        ),
        html.input(
            {
                "class": class_name,
                "value": value,
                "on_change": handle_change
            }),
    )


@ component
def Table(value, set_value):
    rows = []
    for row in food_data:
        name = html.td(row["name"])
        descr = html.td(row["description"])
        tr = html.tr(name, descr, value)
        if not value:
            rows.append(tr)
        elif value.lower() in row["name"].lower():
            rows.append(tr)
        headers = html.tr(
            html.td(
                {"class": "text-2xl font-semibold"},
                "name"
            ),
            html.td(
                {"class": "text-2xl font-semibold"},
                "description"
            )
        )
    table = html.table(html.thead(headers), html.tbody(rows))
    return table


@component
def FilterableList():
    value, set_value = hooks.use_state("")
    children = html._(
        ReturnHomeButton(),
        html.p(Search(value, set_value), html.hr(), Table(value, set_value))
    )
    return Layout(children)
