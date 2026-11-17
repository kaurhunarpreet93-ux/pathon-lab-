mport csv

# Function to display all students
def read_all_students(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)

            print("\n========== ALL ENROLLED STUDENTS ==========")
            print(f"{'Roll No':<10}{'Name':<15}{'Subject':<15}{'Marks':<10}")
            print("-" * 50)

            count = 0
            for row in reader:
                print(f"{row['RollNo']:<10}{row['Name']:<15}{row['Subject']:<15}{row['Marks']:<10}")
                count += 1

            print("-" * 50)
            print("Total Records:", count)

    except FileNotFoundError:
        print("CSV file not found!")


# Function to filter students scoring above 50
def filter_students_above_threshold(filename, threshold=50):
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)

            print("\n====== STUDENTS WITH MARKS > 50 ======")
            print(f"{'Roll No':<10}{'Name':<15}{'Subject':<15}{'Marks':<10}")
            print("-" * 50)

            count = 0
            for row in reader:
                if int(row['Marks']) > threshold:
                    print(f"{row['RollNo']:<10}{row['Name']:<15}{row['Subject']:<15}{row['Marks']:<10}")
                    count += 1

            print("-" * 50)
            print("Qualified Students Count:", count)

    except FileNotFoundError:
        print("CSV file not found!")


# Main program
filename = "students_data.csv"

while True:
    print("\nSelect an Operation:")
    print("1. Display All Students from CSV")
    print("2. Filter Students (Marks > 50)")
    print("3. Exit")

    choice = input("Enter choice (1-3): ")

    if choice == '1':
        read_all_students(filename)

    elif choice == '2':
        filter_students_above_threshold(filename)

    elif choice == '3':
        print("Thank you for using Student Result Analysis System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
