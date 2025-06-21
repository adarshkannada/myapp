import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from pathlib import Path
from loguru import logger

from src.main.config.config_data import Config


class DataDownload:

    def download_file_by_name(self, credentials, file_name: str):
        """this method will download the latest excel file from google drive"""
        
        # Create a Google Drive API service
        service = build('drive', 'v3', credentials=credentials)
        
        # Search for the file by name
        response = service.files().list(q=f"name='{file_name}'", fields='files(id)', corpora="user").execute()
        files = response.get('files', [])

        # If the file exists, download it
        if files:
            file_id = files[0]['id']
            # request = service.files().export_media(fileId=file_id)
            request = service.files().export_media(fileId=file_id,
                                                   mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            file_path = os.path.join(Path(__file__).absolute().parent, file_name)
            with open(file_path, 'wb') as f:
                downloader = MediaIoBaseDownload(f, request)
                done = False
                while not done:
                    status, done = downloader.next_chunk()
                    logger.info(f"Download progress: {int(status.progress() * 100)}%")
            logger.info("File downloaded successfully.")
            return True
        else:
            logger.info("File not found.")
            return False

    def file_rename(self):
        """this method will delete old file and renames the latest downloaded file"""
        source = os.path.join(Path(__file__).absolute().parent, "Expensify")
        logger.info(f"source file is {source}")
        destination = os.path.join(Path(__file__).absolute().parent, "Expensify.xlsx")
        logger.info(destination)
        if os.path.exists(destination):
            os.remove(destination)
        if not os.path.exists(destination):
            os.rename(source, destination)
        else:
            logger.info(f"No renaming file is already present at the path {destination}")



