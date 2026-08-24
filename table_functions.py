import psycopg2
import csv

config = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
}


create_command_for_books = """
        create table if not exists library_books(
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            author VARCHAR(255) NOT NULL,
            year INTEGER,
            ISBN VARCHAR(255) NOT NULL UNIQUE,
            pages INTEGER,
            genre VARCHAR(255),
            quantity INTEGER  
        )
       """


create_command_for_users = """
        create table if not exists library_users(
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            username VARCHAR(255) NOT NULL UNIQUE,
            birth_date DATE,
            email VARCHAR(255) NOT NULL UNIQUE,
            phone_number VARCHAR(255) NOT NULL,
            auth VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
       """
#Táblázat létrehozása és kitöltése
def books_table():
    try:
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            with conn.cursor() as cursor:
                cursor.execute(create_command_for_books)

                with open("books.csv", "r", encoding="utf-8") as csvfile:
                    reader = csv.reader(csvfile, delimiter=";")
                    next(reader)
                    for row in reader:
                        title = row[0]
                        author = row[1]
                        year = row[2]
                        ISBN = row[3]
                        pages = row[4]
                        genre = row[5]
                        quantity = row[6]

                        cursor.execute(
                            "insert into library_books (title, author, year, ISBN, pages, genre, quantity) values (%s, %s, %s, %s, %s, %s, %s)",
                            (title, author, year, ISBN, pages, genre, quantity))

                conn.commit()
                print("Successful upload!")
    except psycopg2.DatabaseError as error:
        print('ERROR', error)
        print(type(error))


def users_table():
    try:
        with psycopg2.connect(**config) as conn:
            print('Connected to the PostgreSQL server.')
            with conn.cursor() as cursor:
                cursor.execute(create_command_for_users)

                with open("library_users.csv", "r", encoding="utf-8") as csvfile:
                    reader = csv.reader(csvfile, delimiter=";")
                    next(reader)
                    for row in reader:
                        name = row[0]
                        username = row[1]
                        birth_date = row[2]
                        email = row[3]
                        phone_number = row[4]
                        auth = row[5]
                        password = row[6]

                        cursor.execute(
                            "insert into library_users(name, username, birth_date, email, phone_number, auth, password) values (%s, %s, %s, %s, %s, %s, %s)",
                            (name, username, birth_date, email, phone_number, auth, password))
                conn.commit()
                print("Successful upload!")
    except psycopg2.DatabaseError as error:
        print('ERROR', error)
        print(type(error))

# users_table()

