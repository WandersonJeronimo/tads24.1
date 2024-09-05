import plotly
import yfinance as yf
import plotly.express as px

def plot_ts (ticker:str
        ) -> plotly.graph_objs._figure.Figure:
    """
    Plots the closing prices of a stock over time.

    Parameters:
    - ticker (str): The stock ticker symbol (e.g., 'AAPL').

    Returns:
    - go.Figure: A Plotly figure object with the closing price line chart.
    """ 
    ticker_sa = ticker + '.SA'
    data = yf.download(ticker_sa) \
        .reset_index() \
        .assign(
            Open = lambda x: round(x['Open'], 2),
            High = lambda x: round(x['High'], 2),
            Low = lambda x: round(x['Low'], 2),
            Close = lambda x: round(x['Close'], 2)
        ) \
        .drop(['Adj Close', 'Volume'], axis = 1)

    fig = px.line(data, x = 'Date', y = 'Close', title = f'{ticker} Closing prices over time'
            )

    return fig