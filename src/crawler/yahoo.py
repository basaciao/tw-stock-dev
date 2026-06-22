import yfinance as yf


def get_stock_price(symbol: str):

    ticker = yf.Ticker(symbol + ".TW")

    hist = ticker.history(period="5d")

    return hist
