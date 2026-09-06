from login_and_registration import login, registration
from create_databases import *
from ascii import book_ascii
from menu_functions import menu

print(book_ascii)
print("\n----------Welcome to the Bookworm Library!----------\n")

make_table(check_tables("library_books"), books_table)
make_table(check_tables("library_users"), users_table)

while True:
    enter = input("Login or register (or q)?:\n").lower()
    if enter == "login":
        is_ok = login()
        if is_ok == "Function completed":
            menu()
        break
    elif enter == "register":
        registration()
    elif enter == "q":
        break
    else:
        print("Invalid input")

# Username: bence.kovacs
# password: Bence123!