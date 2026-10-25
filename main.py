
from books import display_books, save_books, load_books
from dotenv import load_dotenv

load_dotenv()

user_name = input("Enter your name: ")
print(f"Welcome, {user_name}!")

books = load_books()

print(f"You currently have {len(books)} books.")

book_count = int(input("How many new books do you want to add? "))

for i in range(book_count):
    book_name = input(f"Enter the name of book {i + 1}: ")
    books.append(book_name)

save_books(books)
display_books(books)
