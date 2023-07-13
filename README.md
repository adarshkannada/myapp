# MY UTILS
Utility code written for personal use

# Setup
- Install Python 3.10.5
- Install dependencies from requirements.txt
- Install **pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib**
- Basic setup guide https://developers.google.com/sheets/api/quickstart/python
- Required Environment details
 - ENV variable SPREADSHEET_ID: provide the google sheet ID
 - ENV variable SHEET_CELLS: cell range in format '!F35:G48'
 - place the credentials.json file having google sheets details in the folder src/main/config

# Analysis - My Datascience application
- install streamlit, pandas, matplotlib
- place the data excel file at the location <my-utils\src\main\data>
- run streamlit main.py as below
- open the browser with the given local IP address

# Run
- python -s -m src.main.expense_analysis.expense_analyzer 
- python -s - m src.main.util.website_sanity_test
- python -m streamlit run src/main/expense_analysis/main.py
