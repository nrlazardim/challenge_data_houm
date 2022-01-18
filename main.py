from Input.reading_data import HoumChallenge
from utils.config_util import ConfigUtil
from utils.files_utils import FileUtils

if __name__ == "__main__":
    output_directory = ConfigUtil.get_path_from_config('OUTPUT', 'Folder')
    logging_directory = ConfigUtil.get_path_from_config('LOGGING', 'Folder')

    FileUtils.create_directory_if_not_exits(output_directory)
    FileUtils.create_directory_if_not_exits(logging_directory)

    huom_object = HoumChallenge()
    huom_object.grouping_data_by_latitud_longitud()
