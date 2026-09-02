import csv

def create_csv(data):
    file_name = input("Enter file name: ")
    # név ellenőrzése, hogy nem-e létezik már a fájl
    with open(file_name +".csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["id", "title", "author", "year", "isbn", "pages", "genre", "quantity"])
        writer.writerows(data)
