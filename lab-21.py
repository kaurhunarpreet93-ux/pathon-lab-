
import os

def get_document_statistics(filename):
    with open(filename, "r") as file:
        content = file.read()

    line_count = len(content.splitlines())
    word_count = len(content.split())
    char_count = len(content)

    return line_count, word_count, char_count


def display_document(filename):
    with open(filename, "r") as file:
        lines = file.readlines()

    print(f"\n--- Document Preview ({filename}) ---")

    for i, line in enumerate(lines, start=1):
        print(f"{i:3} | {line.rstrip()}")


filename = "document.txt"

if not os.path.exists(filename):
    sample_text = """Artificial Intelligence is transforming modern industries.
Python provides powerful libraries for text processing and data analysis.
Developers use file handling to store and retrieve persistent records.
Modular programming ensures code is clean, reusable, and easy to maintain."""

    with open(filename, "w") as file:
        file.write(sample_text)

print("=" * 45)
print("       DOCUMENT STATISTICS ANALYZER")
print("=" * 45)

while True:
    print("\nSelect an operation:")
    print("1. Calculate Document Statistics")
    print("2. Display Document Content")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        line_count, word_count, char_count = get_document_statistics(filename)

        print("\n========== DOCUMENT REPORT ==========")
        print("Target File      :", filename)
        print("Total Lines      :", line_count)
        print("Total Words      :", word_count)
        print("Total Characters :", char_count)
        print("=" * 40)

    elif choice == "2":
        display_document(filename)

    elif choice == "3":
        print("\nThank you for using Document Statistics Analyzer. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number from 1 to 3.")
