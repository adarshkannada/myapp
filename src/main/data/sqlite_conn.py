import sqlite3
from loguru import logger
import pandas as pd
from src.main.utils.utils import Utils


class Sql:

    def sql_connection(self):
        try:
            conn = sqlite3.connect('finance.db')
            return conn
        except Error:
            print(Error)

    def create_table(self, name: str):
        con = Sql().sql_connection()
        cur = con.cursor()
        # below is incomplete, needs work
        cur.execute(f"CREATE TABLE IF NOT EXISTS {name}(Date str PRIMARY KEY, Home float,"
                    f"Bills float, Shopping float, Food float, Travel float, Clothes float, Fuel float,"
                    f"Gifts float, General float, Investment float, Medicine float, Total float)")

    def load_data_to_table(self, data: any):
        con = Sql().sql_connection()
        logger.info("source dataframe obtained")
        try:
            data.to_sql(name='monthlyExpense', con=con, if_exists='append', index=False)
            logger.info("data loaded into the table")
        except sqlite3.IntegrityError:
            data.to_sql(name='monthlyExpense', con=con, if_exists='replace', index=False)
            Sql().create_table()
        logger.info("dropped, created new table. Data loaded again.")

    def full_load(self):
        con = con = Sql().sql_connection()


# Sql().create_table()
# df = FetchData().fetch_data(rows=32, worksheet=Utils().get_current_month_year(), header_col_num=1)
# print(df)
# Sql().load_data_to_table(data=df)
