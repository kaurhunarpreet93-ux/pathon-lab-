
filename = "report.txt"

sample_text = [
    "Annual Technology and AI Progress Report.",
    "The adoption of Artificial Intelligence accelerated across business units.",
    "AI algorithms improved diagnostic accuracy in healthcare operations.",
    "Data engineering pipelines were upgraded to support real-time data streaming.",
    "The company plans further investments in AI research and machine learning."
]

with open(filename, "w") as file:
    file.write("\n".join(sample_text))


def search_keyword(filename, keyword):
    count = 0

    with open(filename, "r") as file:
        print("\n--- Search Results ---")

        for line_number, line in enumerate(file, start=1):
            occurrences = line.lower().count(keyword.lower())

            if occurrences > 0:
                print(f"Line {line_number} ({occurrences} match): {line.strip()}")
                count += occurrences

    print(f"\n[FOUND] Total occurrences of '{keyword}': {count}")


def display_document(filename):
    with open(filename, "r") as file:
        print("\n--- Full Report Document (report.txt) ---")

        for line_number, line in enumerate(file, start=1):
            print(f"{line_number} | {line.strip()}")


while True:
    print("\nSelect an operation:")
    print("1. Search Keyword in Document")
    print("2. View Full Document")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        keyword = input("Enter keyword to search: ")
        search_keyword(filename, keyword)

    elif choice == "2":
        display_document(filename)

    elif choice == "3":
        print("Thank you for using Keyword Search Utility. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter 1, 2, or 3.")
