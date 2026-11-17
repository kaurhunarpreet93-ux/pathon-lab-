
books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

library_categories = {book[3] for book in books}

student_wishlist = {
    "AI",
    "Cloud Computing",
    "Robotics",
    "Cybersecurity"
}

while True:
    print("\n" + "=" * 45)
    print("       LIBRARY BOOK & CATEGORY MANAGER")
    print("=" * 45)

    print("\nSelect an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        print("\n--- Current Library Catalog (Fixed Records) ---")
        for i, (title, author, year, category) in enumerate(books, start=1):
            print(f'{i}. "{title}" by {author} ({year}) | Genre: {category}')
        print("Total Books:", len(books))

    elif choice == "2":
        print("\n--- Add New Book Record ---")
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        category = input("Enter category/genre: ")

        book = (title, author, year, category)
        books.append(book)
        library_categories.add(category)

        print(f'[SUCCESS] "{title}" added as an immutable catalog record.')
        print(f'[INFO] Category set updated with: "{category}"')

    elif choice == "3":
        print("\n--- Unique Categories Available in Library (Set) ---")
        for category in sorted(library_categories):
            print("-", category)
        print("Total Unique Genres:", len(library_categories))

    elif choice == "4":
        print("\n--- Add Category to Student Wishlist ---")
        category = input("Enter category to add: ")

        if category in student_wishlist:
            print(f'[INFO] "{category}" already exists in wishlist.')
        else:
            student_wishlist.add(category)
            print(f'[SUCCESS] "{category}" added to student wishlist.')

    elif choice == "5":
        print("\n--- Category Gap Analysis ---")

        common = library_categories.intersection(student_wishlist)
        missing = student_wishlist.difference(library_categories)
        all_categories = library_categories.union(student_wishlist)

        print("\nCategories available in both Library and Wishlist:")
        for category in sorted(common):
            print("-", category)

        print("\nCategories requested but missing from Library:")
        for category in sorted(missing):
            print("-", category)

        print("\nAll Unique Categories:")
        for category in sorted(all_categories):
            print("-", category)

        print("\nTotal Common Categories:", len(common))
        print("Total Missing Categories:", len(missing))
        print("Total Unique Categories:", len(all_categories))

    elif choice == "6":
        print("\nThank you for using Library Book & Category Manager!")
        break

    else:
        print("[ERROR] Invalid choice! Please enter a number from 1 to 6.")
