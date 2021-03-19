# Imports
import pandas as pd
import matplotlib.pyplot as plt


def make_candlestick_plot(df: pd.DataFrame, title: str) -> None:
    """
    Make a candlestick plot for the daily data of prices.

    :param pd.DataFrame df: OHLC data of prices
    :param str title: name of the crypto pair to plot
    :return: None
    """
    # Set parameters
    figsize = (16, 9)
    width_bar = 0.75
    width_shadow = 0.05

    # Obtain bull and bear days
    df_bull = df[df['Close'] >= df['Open']]
    df_bear = df[df['Close'] < df['Open']]

    fig = plt.figure(figsize=figsize)

    # Plot bull candles
    plt.bar(df_bull['Date'], df_bull['Close'] - df_bull['Open'], width_bar, df_bull['Open'], color='g')
    plt.bar(df_bull['Date'], df_bull['High'] - df_bull['Close'], width_shadow, df_bull['Close'], color='g')
    plt.bar(df_bull['Date'], df_bull['Low'] - df_bull['Open'], width_shadow, df_bull['Open'], color='g')

    # Plot bear candles
    plt.bar(df_bear['Date'], df_bear['Close'] - df_bear['Open'], width_bar, df_bear['Open'], color='r')
    plt.bar(df_bear['Date'], df_bear['High'] - df_bear['Open'], width_shadow, df_bear['Open'], color='r')
    plt.bar(df_bear['Date'], df_bear['Low'] - df_bear['Close'], width_shadow, df_bear['Close'], color='r')

    # Formatting
    plt.title(title, fontsize=24, weight='bold')
    plt.xlabel('')
    plt.xlabel('')
    plt.xticks(fontsize=16, rotation=90)
    plt.yticks(fontsize=16)
    plt.tight_layout()

    # Save image
    fig.savefig('./fig/fig_{}.png'.format(title))

    return None
