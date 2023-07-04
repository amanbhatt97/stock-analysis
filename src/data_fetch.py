# %%
from datetime import date
from jugaad_data.nse import stock_df

# %%
def get_daily_price(symbol, from_date, to_date, series = 'EQ'):
    return stock_df(symbol, from_date, to_date, series)

# %%



