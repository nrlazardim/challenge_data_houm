from Input.reading_data import HoumChallenge
import logging

if __name__ == "__main__":

    huom_object = HoumChallenge()

    # For testing propouse
    huom_object.filter_by_portal_name(portal_name="Yapo")
    huom_object.filter_by_longitude_latitude(latitude="-33.52414", longitude="-70.77393000000001")
    logging.info("Program Finish")


