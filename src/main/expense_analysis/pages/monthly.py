import streamlit as st

from src.main.expense_analysis.main import load_data

st.markdown("# Monthly Chart ❄️")
st.sidebar.markdown("# Monthly Chart ❄️")

data = load_data(rows=30, worksheet='jun 2023', header_col_num=1)
st.line_chart(data.drop(['Total', 'Comments'], axis=1))
print(data.drop(['Total', 'Comments'], axis=1))
