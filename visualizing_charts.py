import datetime as dt
import mplfinance as mpf
import pandas as pd
import yfinance as yf

start = dt.datetime(2026,3, 5)
end = dt.datetime.now()

# Download data
data = yf.download("AAPL", start=start, end=end)

# FIX: Drop the extra MultiIndex level yfinance added
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.droplevel(1)

# Style
my_style = mpf.make_mpf_style(
    base_mpf_style = "charles",
    marketcolors = mpf.make_marketcolors(up='green', down='red', inherit=True
    ),
    facecolor = 'black',
    figcolor = '#121212',
    gridcolor = 'lightgray',
    gridstyle = '--',
    rc={
        "text.color": "white",         # Title text color
        "axes.labelcolor": "white",    # Axis label text color
        "xtick.color": "white",        # X-axis tick numbers color
        "ytick.color": "white"         # Y-axis tick numbers color
    }
)



# Plot
mpf.plot(data, type="candle", style=my_style, title="AAPL Candlestick Chart")