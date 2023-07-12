import streamlit as st
import pandas as pd
import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()
# Open the Workbook
FILENAME = os.environ.get('SOURCE_FILENAME')
DATA_FOLDER = os.path.join(Path(__file__).absolute().parent.parent, 'data')
FILE_PATH = os.path.join(DATA_FOLDER, FILENAME)


@st.cache_data
def load_data(rows: int, worksheet: str, header_col_num: int):
    xlsx = pd.ExcelFile(FILE_PATH)
    df = pd.read_excel(xlsx, sheet_name=worksheet, header=header_col_num, nrows=rows)
    return df


st.title('My Analytics')
st.markdown("# Home 🎈")
st.sidebar.markdown("# Home 🎈")
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(rows=32, worksheet='jul 2023', header_col_num=1)
data.drop(['Total', 'Comments'], axis=1)
# print(data)
# Notify the reader that the data was successfully loaded.
st.write(data)
# st.dataframe(data.style.highlight_max(axis=0))
data_load_state.text(f'Data for the month')
