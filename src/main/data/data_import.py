from dotenv import load_dotenv
import pandas as pd
import os
from pathlib import Path
from loguru import logger

from src.main.data.data_download import DataDownload
from src.main.data.sqlite_conn import Sql
from src.main.utils.utils import Utils


class ImportData:
    load_dotenv()
    FILENAME = os.environ.get('SOURCE_FILENAME')
    DATA_FOLDER = os.path.join(Path(__file__).absolute().parent.parent, 'data')
    FILE_PATH = os.path.join(DATA_FOLDER, FILENAME)

    # @st.cache_data
    def get_data(_self, rows: int, worksheet: str, header_col_num: int):
        xlsx = pd.ExcelFile(_self.FILE_PATH)
        df = pd.read_excel(xlsx, sheet_name=worksheet, header=header_col_num, nrows=rows)
        df1 = df.drop('Comments', axis=1)
        logger.info("data obtained from the source")
        return df1

    def full_load(self, start_year: int, end_year: int):
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
            ImportData().full_load(start_year=2019, end_year=int(os.environ.get('END_YEAR')))

# ImportData().data_load()