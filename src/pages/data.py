from reactpy import html, component, use_state, use_effect
from src.components.layout import Layout
from src.components.returnhome import ReturnHomeButton
import requests
from datetime import date, timedelta


@component
def Data():
    data, set_data = use_state([])
    loading, set_loading = use_state(True)
    # 直近2週間に公開されて、100より多くストックされている記事のデータ取得
    today = date.today()
    td = timedelta(days=14)
    a_week_ago = today - td
    # QiitaのAPIからデータ取得
    res = use_state(
        f'https://qiita.com/api/v2/items?page=1&per_page=50&query=created:>{a_week_ago}+stocks:>100')

    def get_data():
        r = requests.get(res.value)
        set_loading(False)
        if r.status_code == 200:
            data = r.json()
            set_data(data)
        else:
            print("Fetch Data Error")

    # 初回データの読み込み
    use_effect(get_data, [])

    # データ取得中
    if (loading):
        return Layout(html.h1("Loading..."))

    # Qiitaのデータ取得結果によって、表示内容制御
    if (len(data) > 0):
        display_html = html.div(
            {
                "class": "text-center",
            },
            html.ul(
                [
                    html.li(
                        {
                            "class": "text-xl font-serif my-2",
                        },
                        html.span(
                            {
                                "class": "text-xl my-2 text-blue-500 hover:underline hover:text-blue-700",
                            },
                            html.a(
                                {"href": f"{i['url']} ",
                                 "target": "_blank"},
                                f"{i['title']}",
                            ),
                        ),
                        html.span(
                            f" ( get {i['stocks_count']} stock Count ) "
                        ),
                    ) for i in data
                ])
        )
    else:
        display_html = html.div(
            {
                "class": "text-center text-xl text-red-500 mt-4",
            },
            "Sorry... Fetch No Data Or Happened Error"
        )

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
                "Qiita Titles"
            ),
            html.div(
                {
                    "class": "text-center",
                },
                display_html
            ),
        )
    )
    return Layout(children)
