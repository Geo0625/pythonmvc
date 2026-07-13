import csv
import os

def record(filename, name, grade):
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, grade])
    print(f"Student Name: {name}, Grade: {grade}.\nSuccessfully written to file {filename}")

def read(filename):       
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            print("----------- Student Record -----------") 
            for row in reader:
                print(f"{row[0]} \t {row[1]}")
    except FileNotFoundError:
        print(f"Error! File: \"{filename}\" not found!")

print("Student Information System")
while True:
    print("Menu: \n1. Add Student Record \n2. View Student Record \n3. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter your choice in numerical digit.")
    else:
        if choice == 1:
            f = "Student_Info.csv"
            n = input("Enter Student Name: ").title()
            g = input(f"Enter the Grade of Student {n}: ")

            if not os.path.exists(f):
                print(f"File named \"{f}\" doesn't exist. Creating the file and adding Column Name.")
                record(f, "Name", "Grade")
                print()
            record(f, n, g)
            
        elif choice == 2:
            f = input("Enter FileName: ") + ".csv"
            read(f)
        elif choice == 3:
            print("Exiting program... Bye!")
            break
        else:
            print("Please choose between 1-3!")
    print()
