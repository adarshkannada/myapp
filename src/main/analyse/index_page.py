import streamlit as st
from dotenv import load_dotenv

from src.main.data.core_data import CoreData
from src.main.data.data_import import ImportData
from loguru import logger
from streamlit_echarts import st_echarts

from src.main.data.sqlite_conn import Sql
from src.main.utils.utils import Utils

load_dotenv()


# streamlit app
st.title('My Analytics')
st.markdown("# Home 🎈")
st.sidebar.markdown("# Home 🎈")
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')


# @st.cache_data
def get_data():
    return Sql().get_data_from_table(query=f"select * from Jul2023 where Date = 'Jul2023'")


# data = get_data()

# Notify the reader that the data was successfully loaded.

bardf = Sql().get_data_from_table(query=f"select * from {Utils().get_current_month_year()} where Date = "
                                        f"'{Utils().get_current_month_year()}'")
home_bar = bardf['Home'].values[0]
bills_bar = bardf['Bills'].values[0]
shopping_bar = bardf['Shopping'].values[0]
food_bar = bardf['Food'].values[0]
travel_bar = bardf['Travel'].values[0]
clothes_bar = bardf['Clothes'].values[0]
fuel_bar = bardf['Fuel'].values[0]
gifts_bar = bardf['Gifts'].values[0]
general_bar = bardf['General'].values[0]
invest_bar = bardf['Investment'].values[0]
meds_bar = bardf['Medicine'].values[0]


options = {
    "xAxis": {
        "type": "category",
        "data": CoreData().columns,
    },
    "yAxis": {"type": "value"},
    "series": [{"data": [home_bar, bills_bar, shopping_bar, food_bar, travel_bar, clothes_bar,
                         fuel_bar, gifts_bar, general_bar, invest_bar, meds_bar],
                "type": "bar"}],
}

st.write("# Current Month")
st_echarts(options=options, height="500px")

data_load_state.text(f'Data for the current month')
