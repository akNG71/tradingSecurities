import matplotlib.pyplot as plt
import mplfinance as mpf
import numpy as np
import pandas as pd
import talib as ta
import yfinance as yf

ts_data = yf.Ticker("TATASTEEL.NS")
ts = ts_data.history(
    interval="1d",
    start="2023-08-13",
    end="2025-08-13",
    actions=False,
)
ts.info()

upper, middle, lower = ta.BBANDS(ts.Close, timeperiod=21)
sma_21 = ta.SMA(ts.Close, timeperiod=21)
ts["sma_21"] = sma_21
ts["upper_bb"] = upper
ts["middle_bb"] = middle
ts["lower_bb"] = lower

ts.iloc[-5:, -3:]

# visualize close prices of tata steel
apdict = mpf.make_addplot(ts["sma_21"])
mpf.plot(
    ts, ax=ax1, axtitle="SMA (21)", volume=True, addplot=apdict, style="tradingview"
)
mpf.show()

# bollinger bands
apbb = mpf.make_addplot(ts[["upper_bb", "middle_bb", "lower_bb"]])
mpf.plot(ts, axtitle="Bollinger Bands", volume=True, addplot=apbb)
mpf.show()

# Multiple plots
fig = mpf.figure(figsize=(12, 9))
ax1 = fig.add_subplot(2, 1, 1, style="tradingview")
ax2 = fig.add_subplot(2, 1, 2, style="yahoo")

apdict = mpf.make_addplot(ts["sma_21"])
apbb = mpf.make_addplot(ts[["upper_bb", "middle_bb", "lower_bb"]])
mpf.plot(ts, ax=ax1, axtitle="SMA (21)", addplot=apdict)
mpf.plot(ts, ax=ax2, axtitle="Bollinger Bands", addplot=apbb)
fig.show()

# Create addplots with panel assignment
apds = [
    mpf.make_addplot(ts['sma_21'], color='blue', panel=0),  # Overlay on main candlestick chart
    mpf.make_addplot(ts['upper_bb'], color='red', panel=1),  # Bollinger Bands in 2nd panel
    mpf.make_addplot(ts['middle_bb'], color='orange', panel=1),
    mpf.make_addplot(ts['lower_bb'], color='red', panel=1),
]

# Plot with multiple panels
mpf.plot(
    ts,
    type='candle',
    style='yahoo',
    title='Tata Steel - SMA(21) & Bollinger Bands',
    addplot=apds,
    volume=True,       # volume will be in the last panel automatically
    figscale=1.2,
    figratio=(12, 9),
    panel_ratios=(3, 2 )  # Relative height: SMA panel, BB panel, volume panel
)
mpf.show()
