import streamlit as st
from dotenv import load_dotenv
from src.main.data.data_import import ImportData
from loguru import logger

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
    return Sql().get_data_from_table(query=f"select * from Jul2023 where Date = 'Jul23'")


data = get_data()

# Notify the reader that the data was successfully loaded.
st.write(data)
data_load_state.text(f'Data for the month')


