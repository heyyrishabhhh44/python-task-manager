import csv

FILE_NAME = "data/tasks.csv"

def add_task(employee, task):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([employee, task, "Pending"])

def view_tasks():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
