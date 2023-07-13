import streamlit as st

from src.main.data.fetch_data import FetchData

st.markdown("# Monthly Chart ❄️")
st.sidebar.markdown("# Monthly Chart ❄️")


@st.cache_data
def get_data():
    return FetchData().load_data(rows=32, worksheet='jun 2023', header_col_num=1)


st.markdown("# June 2023")
data = get_data()
st.write(data)

