import constants
import utils

import requests
from bs4 import BeautifulSoup


def main():
    session = requests.Session()
    
    url = input(constants.INSERT_URL)
    file_extension = input(constants.ASK_FILE_EXTENSION)
    destination = input(constants.DESTINATION)

    if constants.ALPHA_JUDGE in url.lower():
        utils.login_alpha_judge(session, constants.alpha_judge_login_url)
        json_response = utils.get_json_from_alpha_url(session, url)
        
        utils.create_directory_with_tasks(
            json_response["contest"]["name"],
            [task["name"] for task in json_response["contest"]["problems"]],
            destination, 
            file_extension
            )
    else:
        utils.login_old_judge(session, constants.old_judge_login_url)

        response = session.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        utils.create_directory_with_tasks(
            utils.get_theme_name(soup),
            [li.find("a").text for li in utils.get_theme_tasks(soup)],
            destination, 
            file_extension
            )


# elif not will_insert_url:
#     utils.select_from_menu(constants.COURSES, constants.COURSE_CHOICE)
#     print()
#     utils.select_from_menu(constants.LANGUAGES, constants.LANGUAGE_CHOICE)


main()