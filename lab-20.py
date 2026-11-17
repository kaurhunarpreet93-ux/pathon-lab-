
def append_entry(filename, entry):
    with open(filename, "a") as file:
        file.write(entry + "\n")
    print(f"[SUCCESS] New entry logged to '{filename}'.")


def display_log(filename):
    print("\n========== DAILY LOG BOOK ==========")

    with open(filename, "r") as file:
        entries = file.readlines()

    if entries:
        for i, entry in enumerate(entries, start=1):
            print(f"[{i:02d}] {entry.strip()}")

        print(f"\nTotal Logged Entries: {len(entries)}")
    else:
        print("No log entries found.")

    print("=" * 40)


filename = "daily_log.txt"

with open(filename, "a") as file:
    pass

print("=" * 40)
print("          OFFICE DAILY LOG BOOK")
print("=" * 40)

while True:
    print("\nSelect an operation:")
    print("1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        entry = input("Enter log entry: ")

        if entry.strip():
            append_entry(filename, entry)
        else:
            print("[ERROR] Log entry cannot be empty.")

    elif choice == "2":
        display_log(filename)

    elif choice == "3":
        print("\nThank you for using the Daily Log Book. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number from 1 to 3.")
