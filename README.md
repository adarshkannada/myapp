# Data Analytics Application
An analytics for personal finance.
Sources Data from Google Sheets, Exposes Data to be used for different Analytics.

# Setup
- Install Python 3.10.5
- Install dependencies from `requirements.txt`

## Google OAuth 2.0 Setup
To run this application, you need to enable the Google Drive API and create OAuth 2.0 credentials for a web application.

1.  **Enable Google Drive API**:
    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a new project or select an existing one.
    - In the navigation menu, go to **APIs & Services > Library**.
    - Search for "Google Drive API" and enable it.

2.  **Create OAuth 2.0 Credentials**:
    - In the Google Cloud Console, go to **APIs & Services > Credentials**.
    - Click **Create Credentials** and select **OAuth client ID**.
    - For the **Application type**, choose **Web application**.
    - Give it a name (e.g., "Personal Finance App").
    - Under **Authorized redirect URIs**, add `http://localhost:8501`. This is the default address for Streamlit applications.
    - Click **Create**.

3.  **Download Credentials**:
    - After creating the credentials, a dialog will appear with your **Client ID** and **Client Secret**.
    - Click the **Download JSON** button to download the credentials file.
    - Rename the downloaded file to `credentials.json`.
    - Place the `credentials.json` file in the `src/main/config/` directory of this project.

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
  - `python -m streamlit run src/main/analyse/index_page.py`
- Open your browser and navigate to `http://localhost:8501`.
- You will be prompted to sign in with your Google account.
- After signing in, you can enter the name of your Google Sheet and download it for analysis.
