from check_table_data import *
from login_registration import *
from create_file import create_csv
from decorators import log_with_comment, auth_check_decorator


def choose_option(dict, title, query):
    while dict:
        print(f"-----Select {title}-----""\n")
        for k, v in dict.items():
            print(f"{k}. {v['column']}")
        question = input(query)
        if question == "q":
            break
        elif question in dict:
            return dict[question]
        else:
            print("Not a valid option!")

def select_column():
    columns = {
        "1": {"column": "title", "function": title},
        "2": {"column": "author", "function": author},
        "3": {"column": "year", "function": year},
        "4": {"column": "isbn", "function": isbn},
        "5": {"column": "pages", "function": pages},
        "6": {"column": "genre", "function": genre},
        "7": {"column": "quantity", "function": quantity}
    }
    return choose_option(columns,"Column", "What do you want to modify? Choose a number or quit(q)!:\n")


def select_where():
    columns_dict =  {
        "0":{"column": "id"},
        "1":{"column": "title"},
        "2":{"column": "author"},
        "3":{"column": "year"},
        "4":{"column": "isbn"},
        "5":{"column": "pages"},
        "6":{"column": "genre"},
        "7":{"column": "quantity"}
    }
    result = choose_option(columns_dict, "Where", "Choose a number or quit(q)!:\n")
    return result["column"]


def filter_books():
    while True:
        want_filter = input("Do you want to filter the data (y/n)?:\n")
        if want_filter == "y":
            filters = {
                "0":{"column": "id"},
                "1":{"column": "title"},
                "2":{"column": "author"},
                "3":{"column": "year"},
                "4":{"column": "isbn"},
                "5":{"column": "pages"},
                "6":{"column": "genre"},
                "7":{"column": "quantity"}
            }
            result = choose_option(filters, "Filter", "Filter by (or quit(q)):\n")
            filter = result["column"]

            if result in filters.values():
                filter_value = input("Value:\n")
                is_data_ok = check_input_data("*", filter, filter_value)

                if is_data_ok == "Data is OK!":
                    select_command = (f"SELECT * FROM library_books "
                                        f"WHERE {filter} = %s")
                    result = database_execute(select_command,(filter_value,),fetch=True)
                    for row in result:
                        print(row)
                    return result
                else:
                    print("No data found!")
            else:
                print("Not a valid option!")
        elif want_filter == "n":
            break
        else:
            print("Not a valid option!")


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
    elif create_file == "n":
        return filtered_data
    else:
        print("Not a valid option!")

@auth_check_decorator("admin")
def modify_data():
    selected_column = select_column()
    column_name = selected_column["column"]
    check_function = selected_column["function"]
    if column_name is None:
        return

    to_what = check_new_data(check_function)

    where_column = select_where()
    if where_column is None:
        return

    where_data = input("Value:\n")
    is_data_ok = check_input_data(column_name,where_column,where_data)
    print(is_data_ok)
    if is_data_ok == "Data is OK!":

        query = (f"UPDATE library_books "
                 f"SET {column_name} = %s"
                 f"WHERE {where_column} = %s")

        data = (to_what, where_data)
        result = database_execute(query,data)
    else:
        print(f"{where_data} is not found in {where_column}!")

@auth_check_decorator("admin")
def delete_books():
    column_name = "*"
    where_column = select_where()
    where_data = input("Value:\n")
    is_data_ok = check_input_data(column_name, where_column, where_data)

    if is_data_ok == "Data is OK!":

        select_command = (f"SELECT * FROM library_books "
                          f"WHERE {where_column} = %s")

        delete_command = (f"DELETE FROM library_books "
                          f"WHERE {where_column} = %s")

        data = (where_data,)
        result = database_execute(select_command,data,fetch=True)
        for row in result:
            print(row)
        want_to_delete = input("Do you want to delete this/these book(s)(y/n)?:\n").lower()
        if want_to_delete == "y":
            delete = database_execute(delete_command,data)
            # törlés után egy fájlba mentse le a törölt adatokat
        elif want_to_delete == "n":
            delete = None
        return delete
    else:
        print(f"{where_data} is not found in {where_column}!")


def get_book_parameters():
    new_title = title()
    new_author = author()
    new_year = year()
    new_ISBN = isbn()
    new_pages = pages()
    new_genre = genre()
    new_quantity = quantity()

    return new_title,new_author,new_year,new_ISBN,new_pages,new_genre,new_quantity


@auth_check_decorator("admin")
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



