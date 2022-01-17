import configparser

from utils.files_utils import FileUtils


class ConfigUtil:

    @staticmethod
    def get_config(section, variable):
        config = configparser.ConfigParser()
        config.read('config_file.ini')
        return config[section][variable]

    @staticmethod
    def get_path_from_config(section, variable):
        return FileUtils.get_path(ConfigUtil.get_config(section, variable))