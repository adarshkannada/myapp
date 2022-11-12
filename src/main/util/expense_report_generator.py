from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = 'C:\Project\myutils\my-utils\src\main\config\keys.json'
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1-TB70kDSqz5f0yv8BcyrqCUewsRqaiqiz8YRfkmYReE'
SAMPLE_RANGE_NAME = 'Nov 2022!F35:G48'


def main():
    # TODO: Change placeholder below to generate authentication credentials. See
    # https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
    # Authorize using one of the following scopes:
    #     'https://www.googleapis.com/auth/drive'
    #     'https://www.googleapis.com/auth/drive.file'
    #     'https://www.googleapis.com/auth/drive.readonly'
    #     'https://www.googleapis.com/auth/spreadsheets'
    #     'https://www.googleapis.com/auth/spreadsheets.readonly'

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        # print(result)
        values = result.get('values', [])
        print(values)
        if not values:
            print('No data found.')
            return
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()
