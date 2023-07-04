# %%
import numpy as np
import pandas as pd
from datetime import *
import logging

import os
import sys


# Get the parent directory by going up one level
parent_directory = os.path.abspath(os.path.join(os.getcwd()))
# Append the parent directory to the system path
sys.path.append(parent_directory)

# %%
from src.data_fetch import get_daily_price
from src.paths import ProjectPaths
from src.symbols import symbols

# %%
project_paths = ProjectPaths(parent_directory)
raw_data_path = project_paths.raw_data
processed_data_path = project_paths.processed_data

# %%
def raw_data(symbol):
    df = get_daily_price(symbol, datetime.now().date() + timedelta(weeks = -52*5), datetime.now().date())
    df = df.sort_values('DATE')
    df.to_pickle(raw_data_path + '/' + symbol)
    return df

# %%
def processed_data(symbol):
    df = get_daily_price(symbol, datetime.now().date() + timedelta(weeks = -52*5), datetime.now().date())
    df = df.sort_values('DATE')
    df = df[['DATE', 'CLOSE', 'VOLUME']]
    df.to_pickle(processed_data_path + '/' + symbol)
    return df

# %%
for symbol in symbols:
    data = raw_data(symbol)
    data = processed_data(symbol)

# %%
def features(data):
    data['dom'] = data['datetime'].dt.day
    data['month'] = data['datetime'].dt.month
    data['year'] = data['datetime'].dt.year
    data['dow'] = data['datetime'].dt.dayofweek

    data['price_dom'] = data['price'] * data['dom']
    data['price_month'] = data['price'] * data['month']
    data['price_year'] = data['price'] * data['year']
    data['price_dow'] = data['price'] * data['dow']

    data['log'] = data['price'].apply(np.log)
    data['sqrt'] = data['price'].apply(np.sqrt)

    # Differencing features (differences wrt prev day same tb)
    for i in range(1, 6):
        data[f'diff_price_{i}'] = data['price'] - data['price'].shift(i)

    # Lags
    for i in range(2, 10):
        data['lag{}'.format(i)] = data['price'].shift(i)

    # Exponential Moving Averages for mcp
    for i in [1,2,3,4,6,8,12,24]:
        data['ewm{}h'.format(i)] = data['price'].ewm(span = i).mean()


    # Covid 1st wave
    data.loc[(data.year == 2020)&(data.month.isin([3,4,5,6,7,8,9])),'covid_first_wave'] = 1
    data['covid_first_wave'] = data['covid_first_wave'].replace(np.nan, 0)

    # Covid 2nd wave
    data.loc[(data.year == 2021)&(data.month.isin([3,4,5,6])),'covid_second_wave'] = 1
    data['covid_second_wave'] = data['covid_second_wave'].replace(np.nan, 0)


    data['target'] = data['price'].shift(-2)
    return data
