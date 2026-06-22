import requests

from config import TWSE_URL


def get_tpex_daily_data(date: str):

    url = f"{TWSE_URL}/exchangeReport/STOCK_DAY_ALL"

    params = {
        "response": "json",
        "date": date.replace("-", "")
    }

    res = requests.get(url, params=params)

    if res.status_code != 200:
        raise Exception("TPEX API error")

    return res.json()
