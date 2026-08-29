from login_registration import *
from create_file import create_csv
from decorators import log_with_comment, auth_check_decorator

def choose_option(dict, title, query):
    while dict:
        print(f"-----Select {title}-----""\n")
        for k, v in dict.items():
            print(f"{k}. {v['column']}")
        question = input(query)
        # check, hogy létezik-e
        if question == "q":
            break
        elif question in dict:
            return dict[question]["column"]

        else:
            print("Not a valid option!")

def select_column_for_modification():
    columns = {
        "1":{"column": "Title"},
        "2":{"column": "Author"},
        "3":{"column": "Year"},
        "4":{"column": "ISBN"},
        "5":{"column": "Pages"},
        "6":{"column": "Genre"},
        "7":{"column": "Quantity"}
    }
        # check, hogy létezik-e
    return choose_option(columns,"Column", "What do you want to modify? Choose a number or quit(q)!:\n")


def select_where():
    columns_dict =  {
        "0":{"column": "ID"},
        "1":{"column": "Title"},
        "2":{"column": "Author"},
        "3":{"column": "Year"},
        "4":{"column": "ISBN"},
        "5":{"column": "Pages"},
        "6":{"column": "Genre"},
        "7":{"column": "Quantity"}
    }
    return choose_option(columns_dict, "Where", "Choose a number or quit(q)!:\n")


def filter_books():
    while True:
        want_filter = input("Do you want to filter the data (y/n)?:\n")
        if want_filter == "y":
            filter_list = ["title", "author", "year", "ISBN", "pages", "genre", "quantity"]
            print("-----FILTER BY-----")
            for i in filter_list:
                print(i)
            filter = input("Filter by:\n").lower()
            if filter in filter_list:
                filter_value = input("Value:\n")
                # beírt adat ellenőrzése hogy megtalálható-e a táblázatban
                select_command = (f"SELECT * FROM library_books "
                                  f"WHERE {filter} = %s")
                result = database_execute(select_command,(filter_value,),fetch=True)
                for row in result:
                    print(row)
                return result
            else:
                print("Not a valid option!")
        else:
            break


@log_with_comment("Listed data.")
def list_books():

    query = "SELECT * FROM library_books order by id"
    result  = database_execute(query, fetch=True)
    for row in result:
        print(row)
    print("\n")
    filtered_data = filter_books()
    create_file = input("Do you want to save the data?(y/n)?:\n").lower()
    if create_file == "y":
        create_csv(filtered_data)
    else:
        return filtered_data

@auth_check_decorator("admin")
@log_with_comment("Modified data.")
def modify_data():
    column_name = select_column_for_modification()
    if column_name is None:
        return
    to_what = input("New data:\n")
    # check, hogy valid data-e
    where_column = select_where()
    if where_column is None:
        return
    # check, hogy létezik-e

    where_data = input("'Where''s data:\n")
    # check, hogy létezik-e

    query = (f"UPDATE library_books "
             f"SET {column_name} = %s"
             f"WHERE {where_column} = %s")

    data = (to_what, where_data)
    result = database_execute(query,data)

# ellenőrizni kell hogy megfelel-e a táblázatban megadott típusnak


@auth_check_decorator("admin")
@log_with_comment("Deleted data.")
def delete_books():
    where_column = select_where()
    where_data = input("'Where''s data:\n")
    select_command = (f"SELECT * FROM library_books "
                      f"WHERE {where_column} = %s")

    delete_command = (f"DELETE FROM library_books "
                      f"WHERE {where_column} = %s")
    data = (where_data,)
    result = database_execute(select_command,data,fetch=True)
    for row in result:
        print(row)
    want_to_delete = input("Do you want to delete this book(y/n)?:\n").lower()
    if want_to_delete == "y":
        delete = database_execute(delete_command,data)
    else:
        delete = None
    return delete

# törlés után egy fájlba mentse le a törölt adatokat


def get_book_parameters():
    title = input("Title:\n")
    author = input("Author:\n")
    year = int(input("Year:\n"))
    ISBN = input("ISBN:\n")
    pages = int(input("Pages:\n"))
    genre = input("Genre:\n")
    quantity = int(input("Quantity:\n"))

    return title,author,year,ISBN,pages,genre,quantity


@auth_check_decorator("admin")
@log_with_comment("Added book to table.")
def add_books():
    title, author, year, ISBN, pages, genre, quantity = get_book_parameters()

    insert_command ="insert into library_books (title, author, year, ISBN, pages, genre, quantity) values (%s, %s, %s, %s, %s, %s, %s)"
    data = (title, author, year, ISBN, pages, genre, quantity)

    database_execute(insert_command,data)


def list_options():
    options = {
        "1":{"option": "List Books","function":list_books},
        "2":{"option": "Modify Books Table","function":modify_data},
        "3":{"option": "Delete Books","function":delete_books},
        "4":{"option": "Add Books","function":add_books}
    }
    return options

def menu():
    options_dict = list_options()
    while options_dict:
        print("-----MENU-----""\n")
        for k,v in options_dict.items():
            print(f"{k}. {v['option']}")
        number = input("\n""Choose option or quit (q)!: ").lower()
        if number == "q":
            break
        elif number in options_dict:
           options_dict[number]["function"]()
        else:
            print("Not a valid option!")



