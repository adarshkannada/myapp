import sqlite3
from loguru import logger
import pandas as pd
from src.main.data.fetch_data import FetchData


class Sql:

    def sql_connection(self):
        try:
            conn = sqlite3.connect('finance.db')
            return conn
        except Error:
            print(Error)

    def create_table(self):
        con = Sql().sql_connection()
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS monthlyExpense(Date str PRIMARY KEY, Home float,"
                    " Bills float, Shopping float, Food float, Travel float, Clothes float, Fuel float, "
                    "Gifts float, General float, Investment float, Medicine float, Total float)")

    def load_data_to_table(self, data: any):
        con = Sql().sql_connection()
        logger.info("source dataframe obtained")
        data.to_sql(name='monthlyExpense', con=con, if_exists='append', index=False)
        logger.info("data loaded into the table")


# Sql().create_table()
df = FetchData().load_data(rows=32, worksheet='Apr 2022', header_col_num=1)
print(df)
Sql().load_data_to_table(data=df)
