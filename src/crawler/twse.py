import pandas as pd
from models.stock_data import StockData
import requests

from config import TWSE_URL


def get_twse_daily_data(date: str):

    url = f"{TWSE_URL}/exchangeReport/STOCK_DAY_ALL"

    params = {
        "response": "json",
        "date": date.replace("-", "")
    }

    res = requests.get(url, params=params)

    if res.status_code != 200:
        raise Exception("TWSE API error")

    data = res.json()

    return data

def get_demo_stock():
    history = pd.DataFrame(
        {
            "Date": [
                "2026-06-20"
            ],      
