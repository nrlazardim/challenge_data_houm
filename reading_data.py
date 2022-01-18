from utils.config_util import ConfigUtil
from datetime import datetime
import pandas as pd
import pytz
import logging
import os


class HoumChallenge:

    @staticmethod
    def timetz(*args):
        """
        Create local timezone to be used into our logs, in my case Argentina - Buenos Aires
        :param args: It is used to pass a non-key worded, variable-length argument list. if should be required
        :return:
        """
        try:
            tz = pytz.timezone('America/Argentina/Buenos_Aires')
            return datetime.now(tz).timetuple()
        except Exception as e:
            logging.error(e)

    @staticmethod
    def initialize_log():
        """
        Create and handle our error and other info
        :return: pass
        """
        log_path = ConfigUtil.get_path_from_config('LOGGING', 'Folder')
        os.makedirs(os.path.dirname(log_path), exist_ok=True)
        os.chmod(log_path, 0o777)
        logging_format = "%(asctime)s %(levelname)s: %(message)s"
        logging_date_format = "%Y-%m-%d %H:%M:%S"
        logging.Formatter.converter = HoumChallenge.timetz
        logging.basicConfig(
            level=logging.INFO,
            format=logging_format,
            datefmt=logging_date_format,
            handlers=[logging.FileHandler(f'{log_path}/log.log', mode='w'), logging.StreamHandler()])
        stream_handler = [h for h in logging.root.handlers if isinstance(h, logging.StreamHandler)][0]
        stream_handler.setLevel(logging.INFO)

    @staticmethod
    def reading_csv() -> pd.DataFrame:
        """
        Read a csv file, drop NaN value and change date format to datetime
        :return: Pandas DataFrame
        """
        try:
            logging.info('Reading CSV File.')
            file = ConfigUtil.get_path_from_config('INPUT', 'Folder') + ConfigUtil.get_config("INPUT", "OriginFile")
            data_set = pd.read_csv(file).dropna()
            data_set["publication_date"] = pd.to_datetime(data_set["publication_date"])
            return data_set
        except Exception as e:
            logging.error(e)

    def __init__(self):
        HoumChallenge.initialize_log()
        self.original_data_set = HoumChallenge.reading_csv()

    def grouping_data_by_latitud_longitud(self):
        """
        Group data by latitude and longitude information. With this group of data, we have the unique
        properties into geographic map
        :return:
        """
        try:
            if self.original_data_set is not None:
                logging.info('Starting Handle Data')
                data_repeat = None

                group = self.original_data_set.groupby(["latitude", "longitude"], as_index=False, sort=False).size()
                tuple_data_set = [(latitude, longitude) if size > 1 else None for latitude,
                                                                                  longitude,
                                                                                  size in zip(group['latitude'],
                                                                                              group['longitude'],
                                                                                              group['size'])]
                logging.info('Getting Duplicates Properties.')
                for value in tuple_data_set:
                    if value is not None:
                        data_repeat = self.original_data_set.loc[
                            (self.original_data_set['latitude'] == value[0]) &
                            (self.original_data_set['longitude'] == value[1])
                            ]
                        # TODO handle this part
                        # logging.info('Saving Data.')
                        # data_repeat.to_csv()

                # data_repeat = data_repeat.merge(pepe, right_index=True, left_index=True, how="outer").dropna()
                # data_repeat = df.loc[(df['latitude'] == -33.4558907) & (df['longitude'] == -70.6305771)]
                # df.pivot_table(index=['publication_title', 'publisher', 'link'], aggfunc='size')
                # data_repeat.to_csv("pepe.csv")

                return data_repeat
        except Exception as e:
            logging.error(e)
