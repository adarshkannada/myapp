import os
from datetime import date
import calendar
from pathlib import Path
from dotenv import load_dotenv
import json


class Config:
    def __init__(self):
        load_dotenv()
        self.working_directory = Path(__file__).absolute().parent
        self.config = {'SERVICE_ACCOUNT_FILE': "credentials.json",
                       'SPREADSHEET_ID': os.environ.get('SPREADSHEET_ID'),
                       'SCOPES': [os.environ.get('SCOPES')],
                       'SHEET_CELLS': os.environ.get('SHEET_CELLS')}
        self.current_date = date.today()

    def get_service_account_file(self):
        return os.path.join(self.working_directory, self.config.get('SERVICE_ACCOUNT_FILE'))

    def get_spreadsheet_id(self):
        return self.config.get('SPREADSHEET_ID')

    def get_scopes(self):
        return self.config.get('SCOPES')

    def get_sheet_cells(self):
        return self.config.get('SHEET_CELLS')

    def get_month(self):
        month = self.current_date.month
        year = self.current_date.year
        month_name = calendar.month_name[month]
        real_month = str(month_name)[0:3] + ' ' + str(year)
        return real_month

    def create_credentials_json(self, file_name):
        credentials = {
            "type": "service_account",
            "project_id": os.environ.get("PROJECT_ID"),
            "private_key_id": os.environ.get("PRIVATE_KEY_ID"),
            "private_key": os.environ.get("PRIVATE_KEY"),
            "client_email": os.environ.get("CLIENT_EMAIL"),
            "client_id": os.environ.get("CLIENT_ID"),
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": os.environ.get("CLIENT_X509_CERT_URL"),
            "universe_domain": "googleapis.com"
        }
        path = os.path.join(Path(__file__).absolute().parent, file_name)
        print(path)
        with open(path, 'w') as json_file:
            json.dump(credentials, json_file)

        print("JSON file created successfully at", path)


# print(Config().get_service_account_file())
# print(Config().get_spreadsheet_id())
# print(Config().get_scopes())
# print(Config().get_sheet_cells())
# Config().create_credentials_json(file_name='creds.json')
