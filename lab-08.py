print("==============================================")
print("           SCHOOL RESULT PROCESSING")
print("==============================================")

student_name = input("Enter Student Name : ")
roll_number = input("Enter Roll Number  : ")

print("\n--- Enter Marks for 5 Subjects (0-100) ---")

marks = []
failed = False

for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))

    if mark < 0 or mark > 100:
        print("Error: Marks must be between 0 and 100.")
        raise SystemExit

    marks.append(mark)

    if mark < 40:
        failed = True

total_marks = sum(marks)
percentage = (total_marks / 500) * 100

if failed:
    result = "FAIL"
    grade = "F"
    remarks = "Failed in one or more subjects"

elif percentage >= 90:
    result = "PASS"
    grade = "A+"
    remarks = "Outstanding"

elif percentage >= 80:
    result = "PASS"
    grade = "A"
    remarks = "Excellent"

elif percentage >= 70:
    result = "PASS"
    grade = "B"
    remarks = "Very Good"

elif percentage >= 60:
    result = "PASS"
    grade = "C"
    remarks = "Good"

elif percentage >= 50:
    result = "PASS"
    grade = "D"
    remarks = "Satisfactory"

elif percentage >= 40:
    result = "PASS"
    grade = "E"
    remarks = "Pass"

else:
    result = "FAIL"
    grade = "F"
    remarks = "Fail"

print("\n==============================================")
print("              STUDENT REPORT CARD")
print("==============================================")
print(f"  Student Name : {student_name}")
print(f"  Roll Number  : {roll_number}")
print("----------------------------------------------")
print(f"  Total Marks  : {total_marks} / 500")
print(f"  Percentage   : {percentage:.2f}%")
print(f"  Result       : {result}")
print(f"  Grade        : {grade}")
print(f"  Remarks      : {remarks}")
print("==============================================")
