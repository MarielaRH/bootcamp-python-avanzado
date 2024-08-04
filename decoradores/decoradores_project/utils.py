import os
import csv
import re


def get_user(file_name):
    # Lee un archivo de una ruta especíifica
    with open(f"{os.path.dirname(__file__)}/{file_name}", "r") as file:
        reader = csv.DictReader(file)  # crea un diccionario con los valores del cvs
        data = list(reader)
    return data


def authenticate(username, password):
    user = {"username": username, "password": password}
    if user in get_user("users.csv"):
        return True
    else:
        return False


def is_valid_password(pwd):
    if re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,}", pwd):
        return True
    else:
        return False
