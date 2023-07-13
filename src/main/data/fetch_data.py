from dotenv import load_dotenv
import pandas as pd
import os
from pathlib import Path


class FetchData:
    load_dotenv()
    FILENAME = os.environ.get('SOURCE_FILENAME')
    DATA_FOLDER = os.path.join(Path(__file__).absolute().parent.parent, 'data')
    FILE_PATH = os.path.join(DATA_FOLDER, FILENAME)

    # @st.cache_data
    def load_data(_self, rows: int, worksheet: str, header_col_num: int):
        xlsx = pd.ExcelFile(_self.FILE_PATH)
        df = pd.read_excel(xlsx, sheet_name=worksheet, header=header_col_num, nrows=rows)
        df1 = df.drop('Comments', axis=1)
        return df1


# data = FetchData().load_data(rows=32, worksheet='jul 2023', header_col_num=1)
# print(data)
