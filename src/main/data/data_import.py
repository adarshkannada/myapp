from dotenv import load_dotenv
import pandas as pd
import os
from pathlib import Path
from loguru import logger
# from sqlalchemy import create_engine
from typing import Optional

from src.main.data.data_download import DataDownload
from src.main.data.sqlite_conn import Sql
from src.main.utils.utils import Utils


class ImportData:
    load_dotenv()
    FILENAME = os.environ.get('SOURCE_FILENAME')  # excel file name
    DATA_FOLDER = os.path.join(Path(__file__).absolute().parent.parent, 'data')  # folder where excel file is present
    FILE_PATH = os.path.join(DATA_FOLDER, FILENAME)  # excel file path
    table_name = 'AllTransactions'

    # @st.cache_data
    def get_data(self, rows: int, worksheet: Optional[str], header_col_num: int):
        """ this method imports excel removes comments column, removes rows greater than 32
        and returns a pandas dataframe """
        # xlsx = pd.ExcelFile(_self.FILE_PATH)
        # df = pd.read_excel(xlsx, sheet_name=worksheet, header=header_col_num, nrows=rows)
        # df1 = df.drop('Comments', axis=1)
        # logger.info("data obtained from the source")

        all_sheets = pd.read_excel(self.FILE_PATH, sheet_name=None, header=header_col_num, nrows=rows)

        # Concatenate DataFrames into a single DataFrame
        all_data = pd.concat(all_sheets.values(), ignore_index=True)
        all_data = all_data.drop('Comments', axis=1)
        all_data = all_data.dropna(subset=['Date'])
        all_data = all_data.fillna(value=0)
        all_data = all_data.astype(dtype=str)

        return all_data

    def full_load_old(self, start_year: int, end_year: int):
        """loads all the months data between [start_year] and [end_year]
        as input by the user and as available from the datasource"""
        for year in range(start_year, end_year):
            for month in range(1, 13):
                try:
                    Sql().create_table(name=Utils().get_month_year(month, year))
                    df = ImportData().get_data(rows=32, worksheet=Utils().get_month_year(month, year), header_col_num=1)
                    Sql().load_data_to_table(table_name=Utils().get_month_year(month, year), data=df)
                    logger.info(f"data loaded for the month-year {(Utils().get_month_year(month, year))}")
                except ValueError:
                    continue
                if month > 12:
                    break
            if year > 2023:
                break

    def full_load(self):
        """loads all the data in different worksheets from the source file to destination
        database"""

        # xlsx = pd.ExcelFile(self.FILE_PATH)
        # logger.info(f"list of worksheets from source {xlsx.sheet_names}")
        # for sheet in xlsx.sheet_names:
        #     try:
        #         Sql().create_table(name=sheet)
        #         df = ImportData().get_data(rows=32, worksheet=sheet, header_col_num=1)
        #         Sql().load_data_to_table(table_name=sheet, data=df)
        #         logger.info(f"data loaded for the month-year {sheet}")
        #     except ValueError:
        #         logger.info(f"Error in data loading")
        # Load Excel Sheets into Pandas DataFrames
        try:
            df = ImportData().get_data(rows=31, worksheet=None, header_col_num=1)
            logger.info("Dataframe prepared by reading the source ")
            Sql().load_data_to_table(table_name=self.table_name, data=df)
            logger.info("all transactions data added to DB")
        except ValueError:
            logger.info(f"Error in preparing the dataframe ")

    def incr_load(self):
        """laods current month data into the database"""
        try:
            Sql().create_table(name=Utils().get_current_month_year())
            df = ImportData().get_data(rows=32, worksheet=Utils().get_current_month_year(), header_col_num=1)
            Sql().load_data_to_table(table_name=Utils().get_current_month_year(), data=df)
            logger.info(f"data loaded for the month-year {(Utils().get_current_month_year())}")
        except Error:
            logger.info("possible failure in create table, data load to table")

    def data_load(self):
        """this is the driver method for either full or incremental data load
        based on the ENV variable [LOAD_TYPE] full or current month data is loaded into the database"""
        if os.environ.get('LOAD_TYPE') == 'incremental':
            logger.info(f"incremental data load is triggered")
            DataDownload().download_file_by_name(file_name='Expensify')
            DataDownload().file_rename()
            ImportData().incr_load()

        if os.environ.get('LOAD_TYPE') == 'full':
            logger.info(f"full data load is triggered")
            DataDownload().download_file_by_name(file_name='Expensify')
            DataDownload().file_rename()
            ImportData().full_load()


# ImportData().data_load()
# Config().create_credentials_json(file_name='creds.json')
# DataDownload().download_file_by_name(file_name='Expensify')
# DataDownload().file_rename()