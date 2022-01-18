import os


class FileUtils:

    @staticmethod
    def get_path(path):
        """
        This method  get path
        :param path:
        :return:
        """
        if not path.endswith('/'):
            return f"{path}/"
        return path

    @staticmethod
    def create_directory_if_not_exits(path):
        """
        This method create directory, it is not exist will be created
        :param path:
        :return:
        """
        exist = os.path.exists(path)

        if not exist:
            os.makedirs(path)

    @staticmethod
    def file_exists(path):
        """
        Check if the file exist
        :param path:
        :return:
        """
        return os.path.isfile(path)