import matplotlib as mp
from src.main.data.data_import import ImportData
from loguru import logger


class DataPlots:
    def define_bar_chart(self):
        df = ImportData().get_data(rows=32, worksheet='jul 2023', header_col_num=1)
        ndf = df.iloc[31].tolist()
        logger.info("the final list of data is fetched")
        logger.info(ndf)
        # n_list = ndf['Jul23'].tolist()
        # print(n_list)


DataPlots().define_bar_chart()
