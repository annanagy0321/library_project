import psycopg2

config = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
}

def list_books():
    pass

def modify_books():
    pass

def delete_books():
    pass

def add_books():
    pass

def quit():
    pass


def list_options():
    print("-----MENU-----""\n")
    options = {
        "1":{"option": "List Books","function":list_books},
        "2":{"option": "Modify Books Table","function":modify_books},
        "3":{"option": "Delete Books","function":delete_books},
        "4":{"option": "Add Books","function":add_books}
    }
    return options

def menu():
    options_dict = list_options()
    while options_dict:
        for k,v in options_dict.items():
            print(f"{k}. {v['option']}")
        number = input("\n""Chose option or quit (q)?: ").lower()
        if number == "q":
            break
        elif number in options_dict:
           options_dict[number]["function"]()
        else:
            print("Not a valid option!")



