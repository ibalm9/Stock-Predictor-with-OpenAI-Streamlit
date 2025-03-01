import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_stock_data(symbol, period='1y'):
    """
    Fetch stock data using yfinance
    """
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period=period)
        return hist, stock.info
    except Exception as e:
        raise Exception(f"Error fetching stock data: {str(e)}")

def prepare_stock_analysis_prompt(stock_data, stock_info):
    """
    Prepare prompt for OpenAI analysis
    """
    current_price = stock_data['Close'].iloc[-1]
    prev_price = stock_data['Close'].iloc[-2]
    price_change = ((current_price - prev_price) / prev_price) * 100

    last_month_data = stock_data.tail(30)
    avg_volume = last_month_data['Volume'].mean()

    prompt = f"""
    Analyze this stock data and predict whether it will go up or down in the short term:

    Company: {stock_info.get('longName', 'Unknown')}
    Current Price: ${current_price:.2f}
    24h Change: {price_change:.2f}%
    Average Volume (30 days): {avg_volume:,.0f}
    52 Week High: ${stock_info.get('fiftyTwoWeekHigh', 0):.2f}
    52 Week Low: ${stock_info.get('fiftyTwoWeekLow', 0):.2f}

    Please provide your analysis in the following JSON format:
    {{
        "prediction": "up",
        "confidence": 0.85,
        "reasoning": "explanation of the analysis",
        "target_price": 150.00,
        "timeframe": "1 week"
    }}
    """
    return prompt