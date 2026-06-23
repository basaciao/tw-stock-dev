from technical.rsi import calculate_rsi


def calculate_all_indicators(stock_df):

    result = {}

    result["RSI"] = calculate_rsi(stock_df)

    return result
