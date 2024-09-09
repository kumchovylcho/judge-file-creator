import constants


def request_notice(func):
    def wrapper(*args, **kwargs):
        print(constants.REQUEST_NOTICE)
        return func(*args, **kwargs)

    return wrapper