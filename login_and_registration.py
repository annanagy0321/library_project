import psycopg2
from check_userdata import *
from decorators import log_with_comment

USER = None

def user_data():
    """User adatainak bekérése."""

    user = username()
    pwd = password()
    return user,pwd


def database_execute(query, data=None, fetch=False):
    """Kapcsolat létrehozása a PostgreSQL adatbázissal. """

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


def check_new_registration(name, email):
    """Az új regisztráció egyedi adatainak ellenőrzése."""

    query = (f"SELECT name email FROM library_users "
             f"WHERE username = %s OR email = %s")

    input_data = (name,email)

    result = database_execute(query, input_data, fetch=True)
    if result:
        print("Username or email already exists!")
        return "Exists"



@log_with_comment("Logged in.")
def login():
    """Bejelentkezés a programba."""

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
        return "Function completed"
    else:
        print("Invalid username or password!")


@log_with_comment("Registered.")
def registration():
    """Új adatok megadása regisztáció során."""

    print("----------Register Form----------\n")

    global USER

    nm = get_valid_data(name)
    usernm = get_valid_data(username)
    bday = get_valid_data(date_of_birth)
    mail = get_valid_data(email)
    pw = get_valid_data(password)
    phone = get_valid_data(phone_number)

    if check_new_registration(usernm, mail) == "Exists":
        return
    else:
        command = ("INSERT INTO library_users("
                    "name, username, birth_date, email, phone_number, password, auth)"
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)")

        data = (nm,usernm,bday,mail,phone,pw,"user")

        database_execute(command, data)
        print("Registration successful!\n")

        USER = usernm
        return "Function completed"

