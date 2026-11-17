
username = input("Enter your username: ")
password = input("Enter your password: ")

print("=" * 42)
print("PASSWORD VALIDATION REPORT")
print("=" * 42)

print("Username:", username)
print("Password:", "*" * len(password))

print("\n--- Validation Rules ---")

length_check = len(password) >= 8
digit_check = any(char.isdigit() for char in password)
uppercase_check = any(char.isupper() for char in password)

print(f"[{'PASS' if length_check else 'FAIL'}] Minimum 8 characters ({len(password)} characters)")
print(f"[{'PASS' if digit_check else 'FAIL'}] At least one digit")
print(f"[{'PASS' if uppercase_check else 'FAIL'}] At least one uppercase letter")

print("\n--- Result ---")

if length_check and digit_check and uppercase_check:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID")

print("=" * 42)
