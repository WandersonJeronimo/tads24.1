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

    data['EMA'] = data['Close'].ewm(span = 52, adjust=False).mean()

    fig = px.line(data, x = 'Date', y = 'Close', title = f'Preço de fechamento de {ticker} '
            )
    fig.add_scatter(x=data['Date'], y=data['EMA'], mode='lines', name=f'EMA ({52})', line=dict(color='orange',  width=3))


    return fig