import streamlit as st

from src.main.data.data_import import ImportData

st.markdown("# Monthly Chart ❄️")
st.sidebar.markdown("# Monthly Chart ❄️")


@st.cache_data
def get_data():
    return ImportData().get_data(rows=32, worksheet='jun 2023', header_col_num=1)


st.markdown("# June 2023")
data = get_data()
st.write(data)

