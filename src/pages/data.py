from reactpy import html, component, use_state, use_effect, event
from src.components.layout import Layout
from src.components.returnhome import ReturnHomeButton
import requests
from datetime import date, timedelta


@component
def pageTitle():
    return html.div(
        {
            "class": "text-center mb-4",
        },
        html.label(
            {
                "class": "text-4xl font-serif text-green-500",
            },
            "Qiita Titles"
        ),
    )


@component
def TableHeader():
    style_table_header_td = ["text-center w-1/3 text-xl font-semibold"]
    return html.tr(
        html.td(
            {"class": style_table_header_td},
            "作成日(from)"
        ),
        html.td(
            {"class": style_table_header_td},
            "作成日(to)"
        ),
        html.td(
            {"class": style_table_header_td},
            "ストック数"
        )
    )


@component
def Titles(data, search_content):
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
                                {"href": f"{i['url']} ", "target": "_blank"},
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
                "class": "text-center text-xl text-red-500 mt-8",
            },
            "Sorry... Fetch No Data Or Happened Error"
        )
    return html.div(
        {
            "class": "text-center",
        },
        html.div(
            {
                "class": "text-md font-semibold mb-8 text-gray-500",
            },
            search_content
        ),
        display_html
    )


# 画面に表示するDummyデータ
dummy_data_obj = {
    "title": "Dummy(Failed Fetch)",
    "url": "https://qiita.com/api/v2/docs",
    "stocks_count": 10
}


@component
def Data():
    # 直近2週間に公開されて、100より多くストックされている記事のデータ取得
    init_to_date = date.today()
    td = timedelta(days=14)
    init_from_date = init_to_date - td
    # 画面で管理する値
    from_date, set_from_date = use_state(str(init_from_date))
    to_date, set_to_date = use_state(str(init_to_date))
    stock_count, set_stock_count = use_state(100)
    search_content, set_search_content = use_state('')
    msg, set_msg = use_state('')
    data, set_data = use_state([])

    # QiitaのAPIからデータ取得
    url, set_url = use_state(
        f'https://qiita.com/api/v2/items?page=1&per_page=50&query=created:>={from_date}+created:<={to_date}+stocks:>={stock_count}')

    def get_data():
        set_search_content(
            f'※{from_date}～{to_date}の作成記事で、ストック数が{stock_count}以上を表示しています')
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            set_data(data)
        else:
            print("Fetch Data Error")
            set_data([dummy_data_obj])

    # 初回データの読み込み
    use_effect(get_data, [])

    # available research button
    def available_research():
        if msg == '':
            return False
        else:
            return True

    # validation helper
    def check_under_one(value=stock_count):
        if not value:
            return True
        if int(value) < 1:
            set_msg("ストック数は1以上を設定してください")
            return True
        return False

    # validation helper
    def check_date_order(from_date, to_date):
        if from_date >= to_date:
            set_msg("作成日(to)は作成日(from)より未来を設定してください")
            return True
        return False

    # validation
    def check_allowed_search(value, field):
        if field == 'from_date':
            if check_date_order(value, to_date):
                return False
            if check_under_one():
                return False
        if field == 'to_date':
            if check_date_order(from_date, value):
                return False
            if check_under_one():
                return False
        if field == 'stock_count':
            if check_under_one(value) or check_date_order(from_date, to_date):
                return False
        set_msg('')
        return True

    # 作成日(from)更新時の処理
    def update_from_date(value):
        set_from_date(value)
        if check_allowed_search(value, 'from_date'):
            set_url(
                f'https://qiita.com/api/v2/items?page=1&per_page=50&query=created:>={value}+created:<={to_date}+stocks:>={stock_count}')

    # 作成日(to)更新時の処理
    def update_to_date(value):
        set_to_date(value)
        if check_allowed_search(value, 'to_date'):
            set_url(
                f'https://qiita.com/api/v2/items?page=1&per_page=50&query=created:>={from_date}+created:<={value}+stocks:>={stock_count}')

    # ストック数更新時の処理
    def update_stock_count(value):
        if not value:
            # invalid literal for int() with base 10: ''
            return
        set_stock_count(value)
        if check_allowed_search(value, 'stock_count'):
            set_url(
                f'https://qiita.com/api/v2/items?page=1&per_page=50&query=created:>={from_date}+created:<={to_date}+stocks:>={value}')

    # テーブルの列要素
    @component
    def TableBody():
        style_table_rows = ["px-2 py-2 rounded-md m-2"]
        from_date_td = html.td(
            html.input(
                {
                    "class": style_table_rows,
                    "type": "date",
                    "value": from_date,
                    "on_change": lambda event:
                    {
                        update_from_date(event["target"]["value"])
                    },
                },
            ),)
        to_date_td = html.td(
            html.input(
                {
                    "class": style_table_rows,
                    "type": "date",
                    "value": to_date,
                    "on_change": lambda event:
                    {
                        update_to_date(event["target"]["value"])
                    }
                },
            )
        )
        stock_count_td = html.td(
            html.input(
                {
                    "class": style_table_rows,
                    "type": "number",
                    "value": stock_count,
                    "on_change": lambda event:
                    {
                        update_stock_count(event["target"]["value"])
                    }
                },
            )
        )
        return html.tr(from_date_td, to_date_td, stock_count_td)

    @component
    def Table():
        # 検索情報設定
        return html.div(
            {"class": "flex justify-center"},
            html.table(
                html.thead(TableHeader()),
                html.tbody(TableBody())
            ),
        )

    @component
    def ValidationMsg():
        # バリデーションメッセージ表示
        return html.div(
            {"class": "text-center font-bold text-red-600 mb-4"},
            msg
        )

    # データ再取得
    def re_get_data():
        get_data()

    @component
    def ReGetButton():
        # 再検索ボタン
        return html.div(
            {"class": "flex justify-center mt-2"},
            html.button(
                {
                    "class": "font-semibold rounded items-center bg-green-400 disabled:bg-gray-400 disabled:text-gray-600 hover:bg-green-600 px-4 py-2 mb-4",
                    "disabled": available_research(),
                    "on_click": lambda event: {re_get_data()}
                },
                "再検索"
            ),
        )

    children = html.div(
        ReturnHomeButton(),
        pageTitle(),
        Table(),  # 検索情報設定
        ValidationMsg(),  # バリデーションメッセージ表示
        ReGetButton(),  # 再検索ボタン
        Titles(data, search_content)  # 取得結果表示
    )
    return Layout(children)
