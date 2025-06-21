import os
import sys
from pathlib import Path

# Add project root to Python path to allow absolute imports from 'src'
# This is needed for running the script directly or with an IDE debugger
project_root = Path(__file__).resolve().parents[3]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

import streamlit as st
from dotenv import load_dotenv
from src.main.analyse import google_auth
from src.main.data.core_data import CoreData
from src.main.data.data_import import ImportData
from loguru import logger
from streamlit_echarts import st_echarts

from src.main.data.sqlite_conn import Sql
from pathlib import Path
from src.main.data.data_download import DataDownload

load_dotenv()

st.set_page_config(layout="wide")

def display_dashboard():
    """Displays the analytics dashboard."""
    st.title('My Analytics')
    st.sidebar.markdown("# Home 🎈")

    query = f"select * from AllTransactions where Date BETWEEN '2025-06-01' and '2025-06-29'"
    bardf = Sql().get_data_from_table(query=query)

    if bardf.empty:
        st.warning("No data found for the selected period. Please download a file with recent data.")
        return

    column_names = bardf.columns.values.tolist()
    
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
    st_echarts(options=options, theme='dark', height="500px", key="main_dashboard_chart")


def main():
    """The main function that runs the Streamlit application."""
    if 'credentials_json' not in st.session_state:
        st.session_state['credentials_json'] = None
    if 'user_info' not in st.session_state:
        st.session_state['user_info'] = None

    if st.query_params.get("code") and not st.session_state['credentials_json']:
        try:
            flow = google_auth.get_google_auth_flow()
            if flow:
                credentials = google_auth.get_credentials(flow, st.query_params['code'])
                st.session_state['credentials_json'] = google_auth.credentials_to_json(credentials)
                st.session_state['user_info'] = google_auth.get_user_info(credentials)
                st.query_params.clear()
                st.rerun()
        except Exception as e:
            st.error(f"An error occurred during authentication: {e}")
            st.session_state['credentials_json'] = None
            st.session_state['user_info'] = None

    if st.session_state['credentials_json']:
        col1, col2 = st.columns([0.85, 0.15])
        with col1:
            st.title("Data Analytics Application")
        with col2:
            st.write(f"Welcome, {st.session_state['user_info'].get('name', 'User')}")
            if st.button("Sign out"):
                st.session_state['credentials_json'] = None
                st.session_state['user_info'] = None
                st.rerun()
        
        st.header("Download Google Sheet")
        file_name = st.text_input("Enter the name of the Google Sheet to download:", "Expensify")
        if st.button("Download File"):
            credentials = google_auth.credentials_from_json(st.session_state['credentials_json'])
            downloader = DataDownload()
            with st.spinner("Downloading file..."):
                download_success = downloader.download_file_by_name(credentials, file_name)
            
            if download_success:
                st.success("File downloaded successfully!")
                with st.spinner("Loading data into database..."):
                    ImportData().data_load()
                st.success("Data loaded successfully!")
                st.rerun()
            else:
                st.error("File not found or an error occurred during download.")

        display_dashboard()

    else:
        st.title("Data Analytics Application")
        st.write("Please sign in to continue.")
        flow = google_auth.get_google_auth_flow()
        if flow:
            auth_url = google_auth.get_auth_url(flow)
            st.link_button("Sign in with Google", auth_url)

if __name__ == '__main__':
    main()

