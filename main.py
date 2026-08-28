from login_registration import *
from create_table_functions import *
from ascii import book_ascii
from menu_functions import menu

print(book_ascii)
print("\n----------Welcome to the Bookworm Library!----------\n")

# Username: bence.kovacs
# password: Bence123!

make_table(check_tables("library_books"), books_table)
make_table(check_tables("library_users"), users_table)

while True:
    enter = input("Login or register (or q)?:\n").lower()
    if enter == "login":
        is_ok = login()
        if is_ok == "logged in":
            menu()
        break
    elif enter == "register":
        registration()
    elif enter == "q":
        break
    else:
        print("Invalid input")

