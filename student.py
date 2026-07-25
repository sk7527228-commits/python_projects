import os
FILE_NAME = "students_data.txt"
def line():
    print("=" * 50)
def calculate_percentage(present, absent):
    total = present + absent
    if total == 0:
        return 0
    return (present / total) * 100
def add_student():
    line()
    print("       MUSA SCHOOL MANAGEMENT")
    line()
    name = input("Student Name     : ")
    father = input("Father Name      : ")
    age = input("Age              : ")
    roll = input("Roll Number      : ")
    phone = input("Phone Number     : ")
    location = input("Location         : ")
    old_class = input("Previous Class   : ")
    new_class = input("New Class        : ")
    present = int(input("Present Days     : "))
    absent = int(input("Absent Days      : "))
    percentage = calculate_percentage(present, absent)
    with open(FILE_NAME, "a") as file:
        file.write("\n")
        file.write("=" * 50 + "\n")
        file.write(" SCHOOL STUDENT RECORD\n")
        file.write("=" * 50 + "\n")
        file.write(f"Name            : {name}\n")
        file.write(f"Father Name     : {father}\n")
        file.write(f"Age             : {age}\n")
        file.write(f"Roll Number     : {roll}\n")
        file.write(f"Phone Number    : {phone}\n")
        file.write(f"Location        : {location}\n")
        file.write(f"Previous Class  : {old_class}\n")
        file.write(f"New Class       : {new_class}\n")
        file.write(f"Present Days    : {present}\n")
        file.write(f"Absent Days     : {absent}\n")
        file.write(f"Attendance      : {round(percentage,2)}%\n")
        file.write("=" * 50 + "\n")
    print("\nRecord Saved Successfully!")
def view_students():
    line()
    print("        ALL STUDENT RECORDS")
    line()
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            print(file.read())
    else:
        print("No Record Found.")
while True:
    line()
    print("     haris information")
    line()
    print("1 - Add Student")
    print("2 - View Students")
    print("3 - Exit")
    line()
    choice = input("Enter Choice : ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Good Bye!")
        break
    else:
        print("Invalid Choice")