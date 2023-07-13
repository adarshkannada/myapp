import streamlit as st
import os
from pathlib import Path
from dotenv import load_dotenv
import schedule
import time
from src.main.data.data_download import download_file_by_name, file_rename
from src.main.data.fetch_data import FetchData

load_dotenv()


def download_data():
    download_file_by_name(file_name='Expensify')
    file_rename()


schedule.every().day.at("00:00", "Asia/Kolkata").do(download_data())  # trigger data download every midnight


# prepare path to data source
FILENAME = os.environ.get('SOURCE_FILENAME')
DATA_FOLDER = os.path.join(Path(__file__).absolute().parent.parent, 'data')
FILE_PATH = os.path.join(DATA_FOLDER, FILENAME)

# streamlit app
st.title('My Analytics')
st.markdown("# Home 🎈")
st.sidebar.markdown("# Home 🎈")
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')


# Load 10,000 rows of data into the dataframe.

@st.cache_data
def get_data():
    return FetchData().load_data(rows=32, worksheet='jul 2023', header_col_num=1)


data = get_data()

# data.drop(['Comments'], axis=1)
# print(data)
# Notify the reader that the data was successfully loaded.
st.write(data)
# st.dataframe(data.style.highlight_max(axis=0))
data_load_state.text(f'Data for the month')
