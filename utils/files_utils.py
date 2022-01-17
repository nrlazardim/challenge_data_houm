import os


class FileUtils:

    @staticmethod
    def get_path(path):
        if not path.endswith('/'):
            return f"{path}/"
        return path

    @staticmethod
    def create_directory_if_not_exits(path):
        exist = os.path.exists(path)

        if not exist:
            os.makedirs(path)

    @staticmethod
    def file_exists(path):
        return os.path.isfile(path)