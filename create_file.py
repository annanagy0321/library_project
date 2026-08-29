import csv

def create_csv(data):
    file_name = input("Enter file name: ")
    with open(file_name +".csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["id", "title", "author", "year", "isbn", "pages", "genre", "quantity"])
        writer.writerows(data)
