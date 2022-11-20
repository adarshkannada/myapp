from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

from src.main.config.config_data import Config

SCOPES = Config().get_scopes()
SERVICE_ACCOUNT_FILE = Config().get_service_account_file()
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = Config().get_spreadsheet_id()
SAMPLE_RANGE_NAME = Config().get_month() + Config().get_sheet_cells()


def main():
    # TODO: Change placeholder below to generate authentication credentials. See
    # https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
    # Authorize using one of the following scopes:
    #     'https://www.googleapis.com/auth/drive'
    #     'https://www.googleapis.com/auth/drive.file'
    #     'https://www.googleapis.com/auth/drive.readonly'
    #     'https://www.googleapis.com/auth/spreadsheets'
    #     'https://www.googleapis.com/auth/spreadsheets.readonly'
    output_list = generate_report(get_data_from_google_sheet())
    write_to_file(output_list)


def get_data_from_google_sheet():
    values = None
    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values')
        if not values:
            print('No data found.')
            return
    except HttpError as err:
        print(err)
    return values


def generate_report(the_list: list):
    """ this method will extract data from the list passed to it and print it in
     combined key value format"""
    output_dict = None
    for element in the_list:
        temp_list = element
        output_dict = ": ".join(map(str, temp_list))
        print(output_dict)
        write_to_file(output_dict)
    return output_dict


def write_to_file(data_input: str):
    file_output = open("expense_report.txt", "a")
    temp_data = str(data_input)
    file_output.write("\n"+temp_data)
    file_output.close()


if __name__ == '__main__':
    main()
