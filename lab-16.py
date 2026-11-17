
history = []

def format_number(num):
    if num == int(num):
        return int(num)
    return num

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def modulus(a, b):
    if b == 0:
        return None
    return a % b

def power(base, exp=2):
    return base ** exp

def display_history():
    print("\n--- Calculation History ---")
    if not history:
        print("No calculations performed yet.")
    else:
        for i, record in enumerate(history, start=1):
            print(f"{i}. {record}")

print("=" * 45)
print("       ENTERPRISE MODULAR UTILITY CALCULATOR")
print("=" * 45)

while True:
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus / Remainder (%)")
    print("6. Power / Exponentiation (Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    if choice == "8":
        print("\nThank you for using Utility Calculator. Goodbye!")
        break

    elif choice == "7":
        display_history()

    elif choice in ["1", "2", "3", "4", "5", "6"]:
        try:
            a = float(input("Enter first number: "))

            if choice == "6":
                exp_input = input("Enter exponent (Press Enter for default 2): ")
                if exp_input.strip() == "":
                    result = power(a)
                    operation = f"{format_number(a)} ** 2"
                else:
                    exp = float(exp_input)
                    result = power(a, exp)
                    operation = f"{format_number(a)} ** {format_number(exp)}"

            else:
                b = float(input("Enter second number: "))

                if choice == "1":
                    result = add(a, b)
                    operation = f"{format_number(a)} + {format_number(b)}"

                elif choice == "2":
                    result = subtract(a, b)
                    operation = f"{format_number(a)} - {format_number(b)}"

                elif choice == "3":
                    result = multiply(a, b)
                    operation = f"{format_number(a)} * {format_number(b)}"

                elif choice == "4":
                    result = divide(a, b)
                    operation = f"{format_number(a)} / {format_number(b)}"

                elif choice == "5":
                    result = modulus(a, b)
                    operation = f"{format_number(a)} % {format_number(b)}"

            if result is None:
                print("[ERROR] Cannot divide or calculate modulus by zero.")
            else:
                result = format_number(result)
                record = f"{operation} = {result}"
                history.append(record)
                print(f"[RESULT] {record}")

        except ValueError:
            print("[ERROR] Invalid input! Please enter valid numbers.")

        except OverflowError:
            print("[ERROR] Result is too large to calculate.")

    else:
        print("[ERROR] Invalid choice! Please enter a number from 1 to 8.")
