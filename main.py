from login import *

print("----------Welcome to the Bookworm Library!----------\n")

# Username: bence.kovacs
# password: Bence123!

enter = input("Login or register?:\n")
if enter == "login":
    # hibakezelés
    login()
elif enter == "register":
    registration()
else:
    quit()

    # ezeket követően a menu kilistázása