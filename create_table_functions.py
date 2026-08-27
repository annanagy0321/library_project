import psycopg2
import csv

def create_tables(file, command, query):

    config = {
        'host': 'localhost',
        'database': 'postgres',
        'user': 'postgres',
        'password': 'postgres',
    }

    try:
        with open(file, "r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            next(reader)

            try:
                with psycopg2.connect(**config) as conn:
                    with conn.cursor() as cursor:
                        cursor.execute(command)
                        cursor.executemany(query, reader)

                    conn.commit()
                    print("Successful upload!")

            except psycopg2.DatabaseError as error:
                print('ERROR', error)
                print(type(error))

    except FileNotFoundError:
        print("File not found.")



def books_table():
    create_command = """
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

    query = """
            INSERT INTO library_books
            (title, author, year, ISBN, pages, genre, quantity)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
    create_tables("library_books.csv", create_command, query)


def users_table():
    create_command= """
            create table if not exists library_users(
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                username VARCHAR(255) NOT NULL UNIQUE,
                birth_date DATE,
                email VARCHAR(255) NOT NULL UNIQUE,
                phone_number VARCHAR(255) NOT NULL,
                auth VARCHAR(255) DEFAULT USER,
                password VARCHAR(255) NOT NULL
            )
           """
    query = """
            insert into library_users(
            name, username, birth_date, email, phone_number, auth, password) 
            values (%s, %s, %s, %s, %s, %s, %s)
        """
    create_tables("library_users.csv", create_command, query)

# books_table()
users_table()