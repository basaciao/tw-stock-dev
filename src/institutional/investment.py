import requests
from config import TWSE_URL


def get_investment_buy_sell(date: str):

    url = f"{TWSE_URL}/fund/T86"

    params = {
        "response": "json",
        "date": date.replace("-", ""),
        "selectType": "ALL"
    }

    res = requests.get(url, params=params)

    if res.status_code != 200:
        raise Exception("Investment data error")

    return res.json()
