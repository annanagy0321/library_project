import datetime
from login_and_registration import database_execute

"""A PostgreSQL library_books táblázata beírni kívánt adatok ellenőrzése."""

def title():
    while True:
        title = input("New title:\n")

        if len(title) > 255:
            print("Title is too long!")
        elif title == "":
            print("Title is empty!")
        else:
            return title

def author():
    while True:
        author = input("New author:\n")
        if len(author) > 255:
            print("Author name is too long!")
        else:
            return author


def year():
    while True:

        year_now = datetime.datetime.now().year
        year = input("New year:\n")
        if year.isdigit():
            year = int(year)
            if 0 > year or year > year_now:
                print("Year is invalid!")
            else:
                return year
        else:
            print("Invalid data!")

def isbn():
    while True:
        isbn = input("New ISBN:\n")
        if len(isbn) == 13:
            return isbn
        else:
            print("Character number is wrong!")


def pages():
    while True:
        pages = input("New pages:\n")
        if pages.isdigit():
            pages = int(pages)
            return pages
        else:
            print("Invalid data!")

def genre():
    while True:
        genre = input("New genre:\n")
        if genre.isdigit():
            print("Invalid data!")
        else:
            return genre

def quantity():
    while True:
        quantity = input("New quantity:\n")
        if quantity.isdigit():
            quantity = int(quantity)
            return quantity
        else:
            print("Invalid data!")


def check_input_data(column_name,where_column,data):
    """A bekért adat létezésének ellenőrzése."""

    query = (f"SELECT {column_name} FROM library_books "
             f"WHERE {where_column} = %s")
    input_data = (data,)

    result = database_execute(query, input_data,fetch=True)
    if result:
        return "Data is OK!"

def check_new_data(func):
    """A bekért adat megfelelésének ellenőrzése."""

    result = func()
    return result
