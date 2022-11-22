import os
from datetime import date
import calendar
from pathlib import Path
from dotenv import load_dotenv


class Config:
    def __init__(self):
        load_dotenv()
        self.working_directory = Path(__file__).absolute().parent
        self.config = {'SERVICE_ACCOUNT_FILE': "/keys.json",
                       'SPREADSHEET_ID': os.getenv('SPREADSHEET_ID'),
                       'SCOPES': ['https://www.googleapis.com/auth/spreadsheets.readonly'],
                       'SHEET_CELLS': os.getenv('SHEET_CELLS')}
        self.current_date = date.today()

    def get_service_account_file(self):
        return str(self.working_directory) + self.config.get('SERVICE_ACCOUNT_FILE')

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

#
# s = Config()
# print(s.get_spreadsheet_id())
