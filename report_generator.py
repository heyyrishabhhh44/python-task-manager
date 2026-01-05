import csv

FILE_NAME = "data/tasks.csv"

def generate_report():
    completed = 0
    pending = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[2] == "Completed":
                completed += 1
            else:
                pending += 1

    print("Completed Tasks:", completed)
    print("Pending Tasks:", pending)
