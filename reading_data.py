import pandas as pd


class ReadingCsvFile:

    @staticmethod
    def reading_csv():
        '''
        This method read a csv file and hablde date format to get uniform data.
        :return: DataFrame
        '''
        # data_repeat = pd.DataFrame()
        df = pd.read_csv("query_result_2021-11-25T16_27_02.44381Z.csv")
        df["publication_date"] = pd.to_datetime(df["publication_date"])
        group = df.groupby(["latitude", "longitude"], as_index=False, sort=False).size()
        data = [(latitude, longitude) if size > 1 else None for latitude, longitude, size in zip(group['latitude'],
                                                                                                 group['longitude'],
                                                                                                 group['size'])]
        for value in data:
            if value is not None:
                data_repeat = df.loc[(df['latitude'] == value[0]) & (df['longitude'] == value[1])]
                # data_repeat = data_repeat.merge(pepe, right_index=True, left_index=True, how="outer").dropna()
        # data_repeat = df.loc[(df['latitude'] == -33.4558907) & (df['longitude'] == -70.6305771)]
        # df.pivot_table(index=['publication_title', 'publisher', 'link'], aggfunc='size')
        # data_repeat.to_csv("pepe.csv")

        return data_repeat


data = ReadingCsvFile()
data.reading_csv()