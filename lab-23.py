
import os

filename = "student_marks.txt"

if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("Aman,85\n")
        file.write("Riya,92\n")
        file.write("Karan,78\n")


def store_student(filename, name, marks):
    with open(filename, "a") as file:
        file.write(f"{name},{marks}\n")

    print(f"[SUCCESS] Record for '{name}' ({marks} marks) stored successfully.")


def display_and_calculate_average(filename):
    if not os.path.exists(filename):
        print("[ERROR] Student records file not found.")
        return

    students = []
    total_marks = 0

    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split(",")

            if len(data) == 2:
                name = data[0]
                marks = int(data[1])
                students.append((name, marks))
                total_marks += marks

    if not students:
        print("[INFO] No student records found.")
        return

    print("\n" + "=" * 55)
    print("             STUDENT MARKS LEDGER")
    print("=" * 55)
    print(f"{'No.':<8}{'Student Name':<20}{'Marks Obtained'}")
    print("-" * 55)

    for i, (name, marks) in enumerate(students, start=1):
        print(f"{i:<8}{name:<20}{marks}")

    average = total_marks / len(students)

    print("-" * 55)
    print(f"Total Students : {len(students)}")
    print(f"Total Marks    : {total_marks}")
    print(f"Class Average  : {average:.2f}")
    print("=" * 55)


while True:
    print("\nSelect an operation:")
    print("1. Display Records & Class Average")
    print("2. Add & Store Student Marks")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        display_and_calculate_average(filename)

    elif choice == "2":
        name = input("Enter Student Name: ")

        try:
            marks = int(input("Enter Marks (0-100): "))

            if 0 <= marks <= 100:
                store_student(filename, name, marks)
            else:
                print("[ERROR] Marks must be between 0 and 100.")

        except ValueError:
            print("[ERROR] Please enter valid integer marks.")

    elif choice == "3":
        print("Thank you for using Student Marks Tool. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter 1, 2, or 3.")
