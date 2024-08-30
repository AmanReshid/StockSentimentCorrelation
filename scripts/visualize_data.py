# visualize_data.py

import pandas as pd
import plotly.express as px

def plot_stock_data(data):
    fig = px.line(data, x=data.index, y=['Close', 'SMA'], title='Stock Price with Moving Average')
    fig.show()

def plot_rsi(data):
    fig = px.line(data, x=data.index, y='RSI', title='Relative Strength Index (RSI)')
    fig.show()

def plot_ema(data):
    fig = px.line(data, x=data.index, y=['Close', 'EMA'], title='Stock Price with Exponential Moving Average')
    fig.show()

def plot_macd(data):
    fig = px.line(data, x=data.index, y=['MACD', 'MACD_Signal'], title='Moving Average Convergence Divergence (MACD)')
    fig.show()
