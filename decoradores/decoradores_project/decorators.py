import functools
from utils import is_valid_password
from utils import authenticate


def authenticated_class(cls):
    @functools.wraps(cls)  # nos permite mantener la referencia de la clase
    def wrapper(*args, **kwargs):
        if authenticate(*args):
            return cls(*args, **kwargs)
        else:
            raise Exception("Unauthorized user")

    return wrapper


def validate_password(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            pwd = args[0].password
        except IndexError:
            raise Exception("Password not found")
        if is_valid_password(pwd):
            return func(*args, **kwargs)
        else:
            return Exception("Invalid password")

    return wrapper
