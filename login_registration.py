import psycopg2
from check_userdata import *

config = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
}

def user_data():
    user = username()
    pwd = password()
    return user,pwd


def database_execute(query, data=None, fetch=False):

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, data)
                if fetch:
                    return cursor.fetchone() # tuple értéket ad vissza

    except psycopg2.DatabaseError as error:
        print(error)


def check_auth(username):
    query = """
         SELECT auth
         FROM library_users
         WHERE username = %s
     """
    result = database_execute(query, (username,), fetch=True)
    if result and result[0] == "user":
        print("Welcome, User!")
        return "user"
    else:
        print("Hello, Admin!")
        return "admin"


def login():
    username, password = user_data()
    query = """
        SELECT username, password
        FROM library_users
        WHERE username = %s AND password = %s
    """
    result = database_execute(query,(username, password),fetch=True)
    if result:
        print("Login successful!")
        check_auth(username)
        return "logged in"
    else:
        print("Invalid username or password!")


def registration():
    print("----------Register Form----------\n")
    nm = name()
    usernm = username()
    bday = date_of_birth()
    mail = email()
    pw = password()
    phone = phone_number()

    command = ("INSERT INTO library_users("
               "name, username, birth_date, email, phone_number, password, auth)"
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")

    data = (nm,usernm,bday,mail,phone,pw,"user")

    database_execute(command, data)
    print("Registration successful!\n")

