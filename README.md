# Data Analytics Application
An analytics for personal finance.
Sources Data from Google Sheets, Exposes Data to be used for different Analytics.

# Setup
- Install Python 3.10.5
- Install dependencies from requirements.txt
- Install **pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib**
- Basic setup guide https://developers.google.com/sheets/api/quickstart/python
  - place the json file having google sheets details in the folder <src/main/config>

- ## variables to connect to google storage
  | KEY                  | VALUE                                                 |
  |----------------------|-------------------------------------------------------|
  | SPREADSHEET_ID       | 1-gogole-sheets-id                                    |
  | SCOPES               | https://www.googleapis.com/auth/spreadsheets.readonly |
  | SOURCE_FILENAME      | filename                                              |
  | SERVICE_EMAIL        | email-d                                               |
  | PRIVATE_GSHEETS_URL  | google-sheets-url                                     |
  | SERVICE_ACCOUNT_FILE | credentials.json                                      |
  | PROJECT_ID           | agumbe                                                |
  | PRIVATE_KEY_ID       | id                                                    |
  | PRIVATE_KEY          | key                                                   |
  | CLIENT_EMAIL         | email                                                 |
  | CLIENT_ID            | client-id                                             |
  | CLIENT_X509_CERT_URL | client-url                                            |

- ## variables needed to import data to database
  | KEY       | VALUE              |
  |-----------|--------------------|
  | LOAD_TYPE | full / incremental |
  | DBNAME    | finance.db         |

# Run
- Data Load
  - SET ENV variable LOAD_TYPE to full/incremental
  - RUN python3 -m main [will trigger the driver method]
- RUN Streamlit server
  - python -m streamlit run src/main/analyse/index_page.py
