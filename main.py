from login_registration import *
from ascii import book_ascii
from menu_functions import menu

print(book_ascii)
print("\n----------Welcome to the Bookworm Library!----------\n")

# Username: bence.kovacs
# password: Bence123!

while True:
    enter = input("Login or register (or q)?:\n").lower()
    if enter == "login":
        is_ok = login()
        if is_ok == "logged in":
            menu()
        break
        #majd ennek megfelelően listázni kell a lehetőségeket
    elif enter == "register":
        registration()
    elif enter == "q":
        break
    else:
        print("Invalid input")

    # ezeket követően a menu kilistázása