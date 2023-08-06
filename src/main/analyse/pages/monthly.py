import streamlit as st
import pandas as pd
from src.main.data.core_data import CoreData
from src.main.data.sqlite_conn import Sql

st.markdown("# Monthly Chart ❄️")
st.sidebar.markdown("# Monthly Chart ❄️")

data_load_state = st.text('Loading data...')
data_load_state.text(f'Data for the months of 2023')

df_jul2023 = Sql().get_data_from_table(query=f"select * from Jul2023 where Date = 'Jul2023'")
df_jun2023 = Sql().get_data_from_table(query=f"select * from Jun2023 where Date = 'Jun2023'")
df_may2023 = Sql().get_data_from_table(query=f"select * from May2023 where Date = 'May2023'")
df_apr2023 = Sql().get_data_from_table(query=f"select * from Apr2023 where Date = 'Apr2023'")
df_mar2023 = Sql().get_data_from_table(query=f"select * from Mar2023 where Date = 'Mar2023'")
df_feb2023 = Sql().get_data_from_table(query=f"select * from Feb2023 where Date = 'Feb2023'")
df_jan2023 = Sql().get_data_from_table(query=f"select * from Jan2023 where Date = 'Jan2023'")

frames = [df_jul2023, df_jun2023, df_may2023, df_apr2023, df_mar2023,
          df_feb2023, df_jan2023]
df_merged = pd.concat(frames)
st.write(df_merged)
for each in CoreData().columns:
    st.line_chart(data=df_merged, x='Date', y=[each],
                  width=0, height=0, use_container_width=True)
