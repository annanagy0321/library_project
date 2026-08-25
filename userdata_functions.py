import re
from datetime import datetime


def match(pattern,variable):
    match = re.fullmatch(pattern, variable)
    if match:
        return variable
    else:
        return "Invalid data!"


def name():
    name = input("Name: ")
    pattern = r"^[a-zA-ZÁÉÍÓÖŐÜÚŰáéíóöőüúű -]+$"
    result = match(pattern,name)
    return result


def username():
    username = input("Username: ")
    pattern = r"^[a-zA-Z0-9_.]{5,}+$"
    result = match(pattern,username)
    return result


def password():
    password = input("Password: ")
    pattern = r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*\W)[a-zA-Z\d\W]{8,}$"
    result = match(pattern,password)
    return result


def email():
    email = input("Email: ")
    pattern = r"^[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    result = match(pattern,email)
    return result


def date_of_birth():
    date_of_birth = input("Date of birth: ")
    pattern = r"\d{4}+[-/]+\d{2}+[-/]+\d{2}"
    try:
        date = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        if date:
            result = match(pattern,date_of_birth)
            return result
    except ValueError:
        return "Invalid date!"


def phone_number():
    phone_number = input("Phone number: ")
    pattern = r'^(\+36|06|36)[ /-]?\d{1,2}[ /-]?\d{3}[ /-]?\d{4}$'
    result = match(pattern,phone_number)
    return result



