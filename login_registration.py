import psycopg2
from check_userdata import *
from decorators import log_with_comment

USER = None

def user_data():
    user = username()
    pwd = password()
    return user,pwd


def database_execute(query, data=None, fetch=False):
    config = {
        'host': 'localhost',
        'database': 'postgres',
        'user': 'postgres',
        'password': 'postgres',
    }

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, data)
                if fetch:
                    return cursor.fetchall()

    except psycopg2.DatabaseError as error:
        print(error)



def login():
    global USER
    username, password = user_data()
    query = """
        SELECT username, password
        FROM library_users
        WHERE username = %s AND password = %s
    """
    result = database_execute(query,(username, password),fetch=True)
    if result:
        print("Login successful!")
        USER = username
        return "logged in"
    else:
        print("Invalid username or password!")



def registration():
    print("----------Register Form----------\n")

    global USER

    nm = get_valid_data(name)
    usernm = get_valid_data(username)
    bday = get_valid_data(date_of_birth)
    mail = get_valid_data(email)
    pw = get_valid_data(password)
    phone = get_valid_data(phone_number)

    command = ("INSERT INTO library_users("
                "name, username, birth_date, email, phone_number, password, auth)"
                "VALUES (%s, %s, %s, %s, %s, %s, %s)")

    data = (nm,usernm,bday,mail,phone,pw,"user")

    database_execute(command, data)
    print("Registration successful!\n")

    USER = usernm

