import configparser

from utils.files_utils import FileUtils


class ConfigUtil:

    @staticmethod
    def get_config(section, variable) -> str:
        """
        This method get the config section to be used in the code
        :param section: Section to get
        :param variable: Variable to get into Section
        :return: str
        """
        config = configparser.ConfigParser()
        config.read('config_file.ini')
        return config[section][variable]

    @staticmethod
    def get_path_from_config(section, variable) -> str:
        """
        This method is for get path from config
        :param section: Section in config file
        :param variable: Variable into section
        :return: str
        """
        return FileUtils.get_path(ConfigUtil.get_config(section, variable))