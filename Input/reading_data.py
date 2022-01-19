from utils.config_util import ConfigUtil
from datetime import datetime
import pandas as pd
import numpy as np
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
            country = pytz.all_timezones
            if ConfigUtil.get_config("INPUT", "TimeZone") in country:
                tz = pytz.timezone('America/Buenos_Aires')
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
        Read a csv file and change date format to datetime for handle model
        :return: Pandas DataFrame
        """
        try:
            logging.info('Reading CSV File.')
            file = ConfigUtil.get_path_from_config('INPUT', 'Folder') + ConfigUtil.get_config("INPUT", "OriginFile")
            data_set = pd.read_csv(file)
            data_set["publication_date"] = pd.to_datetime(data_set["publication_date"])
            return data_set
        except Exception as e:
            logging.error(e)

    def __init__(self):
        HoumChallenge.initialize_log()
        self.original_data_set = HoumChallenge.reading_csv()
        self.empty_dataframe = pd.DataFrame(columns=self.original_data_set.columns)  # TODO to be considered

    def time_property_was_found_on_wich_portal(self):
        """
        This method get how many times a property was found on which portal
        :return: DataFrame
        """
        try:
            if self.original_data_set is not None:
                logging.info('Getting how many times a property was found on which portal')
                duplicated_latitude_longitude = self.original_data_set.duplicated(["latitude",
                                                                                   "longitude"]).value_counts()
                logging.info("Duplicated Data: {} , No-Duplicated Data: {}".format(duplicated_latitude_longitude[1],
                                                                                   duplicated_latitude_longitude[0]))
                # self.original_data_set.drop_duplicates(subset=["latitude", "longitude"], inplace=True)
                groupby_original_data_set_by_origin = self.original_data_set.groupby(["origin"],
                                                                                     as_index=False,
                                                                                     sort=False).size()
                logging.info("\n \n" + "Grouping Data by Origin \n" + str(groupby_original_data_set_by_origin))
                property_was_found_on_wich_portal = self.original_data_set.groupby(["latitude",
                                                                                    "longitude",
                                                                                    "origin"],
                                                                                   as_index=False,
                                                                                   sort=True).size()
                property_was_found_on_wich_portal.index = property_was_found_on_wich_portal[
                    'origin']
                property_was_found_on_wich_portal.drop('origin', axis=1, inplace=True)

                # pivot table
                pivot_table = property_was_found_on_wich_portal.pivot_table(values='size',
                                                                            index=["latitude", "longitude"],
                                                                            columns=property_was_found_on_wich_portal.index,
                                                                            aggfunc=np.sum)

                # Save Data Set
                property_was_found_on_wich_portal.to_csv(ConfigUtil.get_path_from_config('OUTPUT', 'Folder') +
                                                         "times_property_on_portals" + ".csv",
                                                         decimal=',',
                                                         sep=';',
                                                         encoding='utf-8'
                                                         )

                pivot_table.to_csv(ConfigUtil.get_path_from_config('OUTPUT', 'Folder') +
                                   "times_property_on_portals_pivot_table" + ".csv",
                                   decimal=',',
                                   sep=';',
                                   encoding='utf-8')

                logging.info('Data Saved Sucessfuly')

                return property_was_found_on_wich_portal

        except Exception as e:
            logging.error(e)

    def filter_by_portal_name(self, portal_name):
        """

        :param portal_name:
        :return:
        """

        property_on_portal = self.time_property_was_found_on_wich_portal()

        filter_by_portal_name = property_on_portal.filter(like=portal_name, axis=0)

        return filter_by_portal_name

    def filter_by_longitude_latitude(self, latitude, longitude):
        """

        :param latitude:
        :param longitude:
        :return:
        """

        filter_by_longitude_latitude = self.original_data_set.loc[
                    (self.original_data_set['latitude'] == latitude) &
                    (self.original_data_set['longitude'] == longitude)

                ]

        logging.info("\n" + str(filter_by_longitude_latitude))

        return filter_by_longitude_latitude
