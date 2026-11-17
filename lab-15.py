
students = {
    "101": {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [92, 88, 95]
    },
    "103": {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [74, 80, 82]
    }
}

while True:
    print("\n" + "=" * 50)
    print("       STUDENT INFORMATION MANAGEMENT SYSTEM")
    print("=" * 50)

    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        print("\n--- Enrolled Student Records ---")

        for roll, details in students.items():
            print(f"Roll No: {roll} | Name: {details['Name']} | Branch: {details['Branch']} | Sem: {details['Semester']} | Marks: {details['Marks']}")

        print("Total Enrolled Students:", len(students))

    elif choice == "2":
        roll = input("Enter Roll Number to search: ")

        student = students.get(roll)

        if student:
            print(f"\n[FOUND] Record for Roll No {roll}:")
            print("  Name     :", student["Name"])
            print("  Branch   :", student["Branch"])
            print("  Semester :", student["Semester"])
            print("  Marks    :", student["Marks"])
        else:
            print("[ERROR] Student record not found.")

    elif choice == "3":
        print("\n--- Register New Student ---")

        roll = input("Enter Roll Number: ")

        if roll in students:
            print("[ERROR] Roll Number already exists.")
        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch (e.g. BCA AI): ")
            semester = input("Enter Semester: ")

            marks = []

            print("Enter marks obtained in 3 subjects:")
            for i in range(1, 4):
                mark = int(input(f"  Subject {i}: "))
                marks.append(mark)

            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Semester": semester,
                "Marks": marks
            }

            print(f"\n[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ")

        if roll in students:
            print("\n1. Update Name")
            print("2. Update Branch")
            print("3. Update Semester")

            update_choice = input("Enter your choice: ")

            if update_choice == "1":
                students[roll]["Name"] = input("Enter new name: ")
                print("[SUCCESS] Name updated.")

            elif update_choice == "2":
                students[roll]["Branch"] = input("Enter new branch: ")
                print("[SUCCESS] Branch updated.")

            elif update_choice == "3":
                students[roll]["Semester"] = input("Enter new semester: ")
                print("[SUCCESS] Semester updated.")

            else:
                print("[ERROR] Invalid update choice.")

        else:
            print("[ERROR] Student record not found.")

    elif choice == "5":
        roll = input("Enter Roll Number to view performance: ")

        if roll in students:
            student = students[roll]
            marks = student["Marks"]

            total = sum(marks)
            percentage = (total / 300) * 100
            average = total / 3

            print("\n--- Academic Performance Report ---")
            print("Name       :", student["Name"])
            print("Roll No    :", roll)
            print("Marks      :", marks)
            print("Total Marks:", total)
            print("Percentage :", f"{percentage:.2f}%")
            print("Average    :", f"{average:.2f}")

            if all(mark >= 40 for mark in marks):
                print("Result     : PASS")
            else:
                print("Result     : FAIL")

        else:
            print("[ERROR] Student record not found.")

    elif choice == "6":
        roll = input("Enter Roll Number to delete: ")

        student = students.pop(roll, None)

        if student:
            print(f"[SUCCESS] Student '{student['Name']}' record deleted.")
        else:
            print("[ERROR] Student record not found.")

    elif choice == "7":
        print("\nThank you for using Student Information Management System!")
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number from 1 to 7.")
