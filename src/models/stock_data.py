from dataclasses import dataclass

import pandas as pd


@dataclass
class StockData:
    """
    股票歷史資料
    """

    stock_id: str

    stock_name: str

    market: str

    industry: str

    history: pd.DataFrame
