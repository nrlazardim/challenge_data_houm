from Input.reading_data import HoumChallenge
from utils.config_util import ConfigUtil
from utils.files_utils import FileUtils

if __name__ == "__main__":
    output_directory = ConfigUtil.get_path_from_config('OUTPUT', 'Folder')
    logging_directory = ConfigUtil.get_path_from_config('LOGGING', 'Folder')

    FileUtils.create_directory_if_not_exits(output_directory)
    FileUtils.create_directory_if_not_exits(logging_directory)

    huom_object = HoumChallenge()
    huom_object.time_property_was_found_on_wich_portal()

    # For testing propouse
    huom_object.filter_by_portal_name(portal_name="Yapo")
    huom_object.filter_by_longitude_latitude()

