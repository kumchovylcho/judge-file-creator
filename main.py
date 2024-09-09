import constants
import utils

import requests
from bs4 import BeautifulSoup


def main():
    session = requests.Session()
    utils.login(session, constants.login_url)

    url = input(constants.INSERT_URL)
    file_extension = input(constants.ASK_FILE_EXTENSION)
    destination = input(constants.DESTINATION)

    response = session.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    utils.create_directory_with_tasks(soup, destination, file_extension)


# elif not will_insert_url:
#     utils.select_from_menu(constants.COURSES, constants.COURSE_CHOICE)
#     print()
#     utils.select_from_menu(constants.LANGUAGES, constants.LANGUAGE_CHOICE)


main()