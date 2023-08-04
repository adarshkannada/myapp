import matplotlib as mp
from src.main.data.data_import import ImportData
from loguru import logger

from src.main.data.sqlite_conn import Sql


class DataPlots:
    def define_bar_chart(self):
        df = Sql().get_data_from_table(query=f"select * from Jul2023 where Date = 'Jul23'")
        ndf = df.iloc[31].tolist()
        logger.info("the final list of data is fetched")
        logger.info(ndf)
        # n_list = ndf['Jul23'].tolist()
        # print(n_list)


DataPlots().define_bar_chart()
