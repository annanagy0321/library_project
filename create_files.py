import csv
import pandas as pd

def file_for_deleted_books(data):

    with open("deleted_books.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["id", "title", "author", "year", "isbn", "pages", "genre", "quantity"])
        writer.writerows(data)
        print("File created successfully!")



def save_filtered_data(data):
    file_name = input("Enter file name: ")
    df = pd.DataFrame(
        data,
        columns=["id", "title", "author", "year", "isbn", "pages", "genre", "quantity"]
    )
    df.to_excel(file_name + ".xlsx", index=False)

    print("File created successfully!")
