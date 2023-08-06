# MY UTILS
Utility code written for personal use

# Setup
- Install Python 3.10.5
- Install dependencies from requirements.txt
- Install **pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib**
- Basic setup guide https://developers.google.com/sheets/api/quickstart/python
  - place the credentials.json file having google sheets details in the folder <src/main/config>
- set the environment variables appropriately

# Run
- Data Load
  - SET ENV variable LOAD_TYPE to full/incremental
  - RUN python3 -m src.main.data.data_import
- RUN Streamlit server
  - python -m streamlit run src/main/analyse/main.py
