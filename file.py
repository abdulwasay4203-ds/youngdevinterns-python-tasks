# Write and read student records using file handling

def write_student():
    file = open("students.txt", "a")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")
    file.write(name + "," + marks + "\n")
    file.close()
    print("Record saved!\n")

def read_students():
    print("\nAll Student Records:")
    file = open("students.txt", "r")
    for line in file:
        name, marks = line.strip().split(",")
        print(f"Name: {name}, Marks: {marks}")
    file.close()

while True:
    print("\n1. Add record")
    print("2. Show records")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        write_student()
    elif choice == "2":
        read_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
