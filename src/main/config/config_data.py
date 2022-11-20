from datetime import date
import calendar


class Config:
    def __init__(self):
        self.config = {'SERVICE_ACCOUNT_FILE': "/home/freedom/Documents/Projects/my-utils/src/main/config/keys.json",
                       'SPREADSHEET_ID': 'id',
                       'SCOPES': ['https://www.googleapis.com/auth/spreadsheets.readonly'],
                       'SHEET_CELLS': '!F35:G48'}
        self.current_date = date.today()

    def get_service_account_file(self):
        return self.config.get('SERVICE_ACCOUNT_FILE')

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









