from requests import Response, Session
from bs4 import BeautifulSoup
import os

import decorators
from constants import CONFIG, PYTHON_EXTENSION


@decorators.request_notice
def login(session: Session, url: str) -> Response:
    response = session.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    csrf_token = soup.find('input', {'type': 'hidden', 'name': "__RequestVerificationToken"}).get("value")

    login_data = {
        'UserName': CONFIG["username"],  # replace with your judge username
        'Password': CONFIG["password"],  # replace with your judge password
        '__RequestVerificationToken': csrf_token
    }
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3673.0 Safari/537.36",
        'Referer': url  # referer header might be required for security reasons
    }

    return session.post(url, data=login_data, headers=headers)


def get_theme_name(soup: BeautifulSoup) -> str:
    return soup.find("h1").find("a").text


def get_theme_tasks(soup: BeautifulSoup):
    return soup.find("div", id="SubmissionsTabStrip").find("ul").find_all("li")


def create_directory_with_tasks(soup: BeautifulSoup, destination: str, file_extension: str):
    file_extension = file_extension.lower().replace(".", "")

    folder_with_task_names = os.path.join(destination, get_theme_name(soup))
    if not os.path.exists(folder_with_task_names):
        os.mkdir(folder_with_task_names)

    for li in get_theme_tasks(soup):
        task_name = li.find("a").text
        task_name = to_snake_case(task_name) if PYTHON_EXTENSION in file_extension else to_pascal_case(task_name)

        end_point = os.path.join(folder_with_task_names, f"{task_name}.{file_extension}")
        # creates empty file
        with open(end_point, "w") as _:
            pass



def select_from_menu(info: list[str], menu: str) -> str:
    print("\n".join(info))
    return input(menu)


def will_insert_url(ask_msg: str, expect_choice: str) -> bool:
    return input(ask_msg).lower() == expect_choice


def sanitize_task_name(task_name: str) -> str:
    return task_name.replace(".", " ").replace("\t", " ")


def to_pascal_case(text: str) -> str:
    return "".join(x.capitalize()
                   for x in
                   sanitize_task_name(text.lower())
                   .split()
                   )


def to_snake_case(text: str) -> str:
    return "_".join(
        sanitize_task_name(text.lower())
        .split()
    )