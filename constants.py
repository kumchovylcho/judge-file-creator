from dotenv import dotenv_values

######################### LOGIN CREDENTIALS #################################

CONFIG = dotenv_values()

############################### ENDPOINTS #############################

old_judge_login_url = "https://judge.softuni.org/Account/Login"
alpha_judge_login_url = "https://alpha.judge.softuni.org/api/account/Login"


############################### CONSTANT STRINGS #############################
REQUEST_NOTICE = "Request has been made, please wait.."
NAVIGATE_OR_URL = "Do you want to insert DIRECT URL or do you want to navigate? (insert/navigate): "
DIRECT = "insert"
INSERT_URL = "Insert URL: "

ALPHA_JUDGE = "alpha.judge"
ALPHA_JUDGE_JSON_BASE_URL = "https://alpha.judge.softuni.org/api/compete/"

EXTENSIONS = [".js", ".py", ".cs", ".java"]
PYTHON_EXTENSION = "py"
ASK_FILE_EXTENSION = "Please provide the file extension your files to be created with: \n" + '\n'.join(EXTENSIONS) + "\n"

DESTINATION = "Path to where it should create the files or . for current directory: "

COURSES = [
    "1. Programming Basics",
    "2. Fundamentals",
    "3. Advanced",
]

LANGUAGES = [
    "1. Javascript",
    "2. Python",
    "3. Java",
    "4. C#"
]

COURSE_CHOICE = f"Choose your course (from 1 to {len(COURSES)}): "
LANGUAGE_CHOICE = f"Choose your language (from 1 to {len(LANGUAGES)}): "


############################### MAPPINGS #############################
CHOICE_TO_COURSE = {
    "1": "Basics",
    "2": "Fundamentals",
    "3": "Advanced"
}

COURSE_TO_ENDPOINT = {
    "Programming Basics": "https://judge.softuni.org/Contests/#!/List/ByCategory/15/Programming-Basics",
    "Fundamentals": "https://judge.softuni.org/Contests/#!/List/ByCategory/40/Fundamentals",
    "Advanced": {
        "Javascript": "https://judge.softuni.org/Contests/#!/List/ByCategory/160/JS-Advanced",
        "Java": "https://judge.softuni.org/Contests/#!/List/ByCategory/44/Java-Advanced",
        "C#": "https://judge.softuni.org/Contests/#!/List/ByCategory/179/CSharp-Advanced",
        "Python": "https://judge.softuni.org/Contests/#!/List/ByCategory/196/Python-Advanced"
    }
}
