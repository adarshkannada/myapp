import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import pandas as pd
from src.main.config.config_data import Config
import os
from pathlib import Path


# Load credentials from the JSON file
CREDENTIALS_FILE = Config().get_service_account_file()  # path of the credentials.json file
credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE,
                                                                    scopes=['https://www.googleapis.com/auth/drive'])

# Create a Google Drive API service
service = build('drive', 'v3', credentials=credentials)
sheet_id = 'id1XqOtPkiE_Q0dfGSoyxrH730RkwrTczcRbDeJJpqRByQid'  # use correct id


def download_file_by_name(file_name):
    """this method will download the latest excel file from google drive"""
    # Search for the file by name
    response = service.files().list(q=f"name='{file_name}'", fields='files(id)').execute()
    files = response.get('files', [])

    # If the file exists, download it
    if files:
        file_id = files[0]['id']
        # request = service.files().export_media(fileId=file_id)
        request = service.files().export_media(fileId=file_id,
                                               mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        file_path = os.path.join(os.getcwd(), file_name)
        with open(file_path, 'wb') as f:
            downloader = MediaIoBaseDownload(f, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                print(f"Download progress: {int(status.progress() * 100)}%")
        print("File downloaded successfully.")
    else:
        print("File not found.")


def file_rename():
    """this method will delete old file and renames the latest downloaded file"""
    source = os.path.join(Path(__file__).absolute().parent, "Expensify")
    print(source)
    destination = os.path.join(Path(__file__).absolute().parent, "Expensify.xlsx")
    print(destination)
    os.remove(destination)
    if not os.path.exists(destination):
        os.rename(source, destination)
    else:
        print(f"No renaming file is already present at the path {destination}")


# Call the function with the file name
download_file_by_name(file_name='Expensify')
file_rename()

