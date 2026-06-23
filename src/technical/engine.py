from models.stock_data import StockData
from technical.rsi import calculate_rsi


def calculate_all_indicators(stock: StockData):

    result = {}

    result["RSI"] = calculate_rsi(stock)

    return result
