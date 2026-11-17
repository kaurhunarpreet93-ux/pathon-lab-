employee_name = input("Enter Employee Name: ")
print("  Data type:", type(employee_name))

employee_id = int(input("Enter Employee ID: "))
print("  Data type:", type(employee_id))

salary = float(input("Enter Salary: "))
print("  Data type:", type(salary))

department = input("Enter Department: ")
print("  Data type:", type(department))

active_input = input("Is the employee active? (yes/no): ").lower()
is_active = active_input == "yes"
print("  Data type:", type(is_active))

print("\n--- Employee Details ---")
print("Name       :", employee_name)
print("ID         :", employee_id)
print("Salary     :", salary)
print("Department :", department)
print("Active     :", is_active)
