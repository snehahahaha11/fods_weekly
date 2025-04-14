import csv
import os
from datetime import datetime, timedelta

class Book:
    def __init__(self, book_id="", title="", author="", publisher="", 
                 is_available=True, issued_to="", issue_date="", return_date=""):
      
        self.book_id = book_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.is_available = is_available
        self.issued_to = issued_to
        self.issue_date = issue_date
        self.return_date = return_date
    
    def display_info(self):
       
        status = "Available" if self.is_available else f"Issued to {self.issued_to}"
        print(f"ID: {self.book_id} | Title: {self.title}")
        print(f"Author: {self.author} | Publisher: {self.publisher}")
        print(f"Status: {status}")
        
        if not self.is_available:
            print(f"Issue Date: {self.issue_date} | Return Date: {self.return_date}")
    
    def to_dict(self):
        
        return {
            'Book ID': self.book_id,
            'Title': self.title,
            'Author': self.author,
            'Publisher': self.publisher,
            'Available': str(self.is_available),
            'Issued To': self.issued_to,
            'Issue Date': self.issue_date,
            'Return Date': self.return_date
        }
    
    @classmethod
    def from_dict(cls, data):
       
        return cls(
            book_id=data.get('Book ID', ''),
            title=data.get('Title', ''),
            author=data.get('Author', ''),
            publisher=data.get('Publisher', ''),
            is_available=data.get('Available', 'True').lower() == 'true',
            issued_to=data.get('Issued To', ''),
            issue_date=data.get('Issue Date', ''),
            return_date=data.get('Return Date', '')
        )


class Person:
  
    
    def __init__(self, person_id="", name="", contact=""):
       
        self.person_id = person_id
        self.name = name
        self.contact = contact
        self.books_borrowed = []
    
    def display_info(self):
       
        print(f"ID: {self.person_id} | Name: {self.name}")
        print(f"Contact: {self.contact}")
        print(f"Books Borrowed: {len(self.books_borrowed)}")
    
    def to_dict(self):
        
        return {
            'Person ID': self.person_id,
            'Name': self.name,
            'Contact': self.contact,
            'Books Borrowed': ','.join(self.books_borrowed)
        }
    
    @classmethod
    def from_dict(cls, data):
       
        person = cls(
            person_id=data.get('Person ID', ''),
            name=data.get('Name', ''),
            contact=data.get('Contact', '')
        )
        books_str = data.get('Books Borrowed', '')
        if books_str:
            person.books_borrowed = books_str.split(',')
        return person


class Library:
   
    
    def __init__(self, books_file="books.csv", people_file="borrowers.csv"):
        
        self.books_file = books_file
        self.people_file = people_file
        self.books = {}
        self.people = {}
        
        
        self.load_data()
    
    def load_data(self):
        
       
        try:
            if os.path.exists(self.books_file):
                with open(self.books_file, 'r', newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        book = Book.from_dict(row)
                        self.books[book.book_id] = book
                print(f"Loaded {len(self.books)} books from file.")
            else:
                print("No existing books data found.")
        except Exception as e:
            print(f"Error loading books data: {e}")
        
     
        try:
            if os.path.exists(self.people_file):
                with open(self.people_file, 'r', newline='') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        person = Person.from_dict(row)
                        self.people[person.person_id] = person
                print(f"Loaded {len(self.people)} borrowers from file.")
            else:
                print("No existing borrowers data found.")
        except Exception as e:
            print(f"Error loading borrowers data: {e}")
    
    def save_data(self):
       
        try:
            with open(self.books_file, 'w', newline='') as file:
                fieldnames = ['Book ID', 'Title', 'Author', 'Publisher', 
                             'Available', 'Issued To', 'Issue Date', 'Return Date']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for book in self.books.values():
                    writer.writerow(book.to_dict())
            print(f"Books data saved to {self.books_file}")
        except Exception as e:
            print(f"Error saving books data: {e}")
        
       
        try:
            with open(self.people_file, 'w', newline='') as file:
                fieldnames = ['Person ID', 'Name', 'Contact', 'Books Borrowed']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for person in self.people.values():
                    writer.writerow(person.to_dict())
            print(f"Borrowers data saved to {self.people_file}")
        except Exception as e:
            print(f"Error saving borrowers data: {e}")
    
    def add_book(self):
        
        try:
            print("\nAdd New Book:")
            print("-" * 20)
            
            book_id = input("Enter Book ID: ")
            
           
            if book_id in self.books:
                print("Error: A book with this ID already exists.")
                return
                
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            publisher = input("Enter Publisher: ")
            
           
            book = Book(book_id, title, author, publisher)
            self.books[book_id] = book
            
            print("Book added successfully!")
            
        except Exception as e:
            print(f"Error adding book: {e}")
    
    def add_borrower(self):
        
        try:
            print("\nAdd New Borrower:")
            print("-" * 20)
            
           
            person_id = input("Enter Borrower ID: ")
            
          
            if person_id in self.people:
                print("Error: A borrower with this ID already exists.")
                return
                
            name = input("Enter Name: ")
            contact = input("Enter Contact Information: ")
            
       
            person = Person(person_id, name, contact)
            self.people[person_id] = person
            
            print("Borrower added successfully!")
            
        except Exception as e:
            print(f"Error adding borrower: {e}")
    
    def issue_book(self):
        
        try:
            print("\nIssue Book:")
            print("-" * 20)
            
            book_id = input("Enter Book ID: ")
            if book_id not in self.books:
                print("Error: Book not found.")
                return
                
            book = self.books[book_id]
            if not book.is_available:
                print(f"Error: Book is already issued to {book.issued_to}.")
                return
            
          
            person_id = input("Enter Borrower ID: ")
            if person_id not in self.people:
                print("Error: Borrower not found.")
                return
                
            person = self.people[person_id]
            
            
            issue_date = datetime.now()
            return_date = issue_date + timedelta(days=7)  
            
         
            book.is_available = False
            book.issued_to = person_id
            book.issue_date = issue_date.strftime("%Y-%m-%d")
            book.return_date = return_date.strftime("%Y-%m-%d")
            
           
            person.books_borrowed.append(book_id)
            
            print(f"Book '{book.title}' issued to {person.name} successfully!")
            print(f"Return Date: {book.return_date}")
            
        except Exception as e:
            print(f"Error issuing book: {e}")
    
    def return_book(self):
        
        try:
            print("\nReturn Book:")
            print("-" * 20)
            
            
            book_id = input("Enter Book ID: ")
            if book_id not in self.books:
                print("Error: Book not found.")
                return
                
            book = self.books[book_id]
            if book.is_available:
                print("Error: This book is not currently issued to anyone.")
                return
            
        
            person_id = book.issued_to
            if person_id in self.people:
                person = self.people[person_id]
                
                
                if book_id in person.books_borrowed:
                    person.books_borrowed.remove(book_id)
            
          
            book.is_available = True
            book.issued_to = ""
            book.issue_date = ""
            book.return_date = ""
            
            print(f"Book '{book.title}' returned successfully!")
            
        except Exception as e:
            print(f"Error returning book: {e}")
    
    def search_book(self):
       
        try:
            print("\nSearch Book:")
            print("-" * 20)
            print("1. Search by ID")
            print("2. Search by Title")
            print("3. Search by Author")
            
            choice = input("\nEnter your choice (1-3): ")
            
            results = []
            
            if choice == '1':
                book_id = input("Enter Book ID: ")
                if book_id in self.books:
                    results.append(self.books[book_id])
            
            elif choice == '2':
                title = input("Enter Title (or part of title): ").lower()
                for book in self.books.values():
                    if title in book.title.lower():
                        results.append(book)
            
            elif choice == '3':
                author = input("Enter Author (or part of author name): ").lower()
                for book in self.books.values():
                    if author in book.author.lower():
                        results.append(book)
            
            else:
                print("Invalid choice.")
                return
            
            if results:
                print(f"\nFound {len(results)} book(s):")
                print("=" * 50)
                for i, book in enumerate(results, 1):
                    print(f"\nBook #{i}:")
                    book.display_info()
                    print("-" * 50)
            else:
                print("No books found matching your criteria.")
            
        except Exception as e:
            print(f"Error searching books: {e}")
    
    def display_all_books(self):
        
        if not self.books:
            print("No books in the library.")
            return
            
        try:
            print("\nAll Books in Library:")
            print("=" * 50)
            for i, book in enumerate(self.books.values(), 1):
                print(f"\nBook #{i}:")
                book.display_info()
                print("-" * 50)
                
        except Exception as e:
            print(f"Error displaying books: {e}")
    
    def display_borrowers(self):
       
        if not self.people:
            print("No borrowers in the system.")
            return
            
        try:
            print("\nAll Borrowers:")
            print("=" * 50)
            for i, person in enumerate(self.people.values(), 1):
                print(f"\nBorrower #{i}:")
                person.display_info()
                
               
                if person.books_borrowed:
                    print("\nCurrently Borrowed Books:")
                    for j, book_id in enumerate(person.books_borrowed, 1):
                        if book_id in self.books:
                            book = self.books[book_id]
                            print(f"  {j}. {book.title} (ID: {book.book_id})")
                
                print("-" * 50)
                
        except Exception as e:
            print(f"Error displaying borrowers: {e}")


def main():
    
    library = Library()
    
    while True:
        try:
            print("\nLibrary Management System")
            print("=" * 30)
            print("1. Add New Book")
            print("2. Add New Borrower")
            print("3. Issue Book")
            print("4. Return Book")
            print("5. Search Book")
            print("6. Display All Books")
            print("7. Display All Borrowers")
            print("8. Save and Exit")
            
            choice = input("\nEnter your choice (1-8): ")
            
            if choice == '1':
                library.add_book()
            elif choice == '2':
                library.add_borrower()
            elif choice == '3':
                library.issue_book()
            elif choice == '4':
                library.return_book()
            elif choice == '5':
                library.search_book()
            elif choice == '6':
                library.display_all_books()
            elif choice == '7':
                library.display_borrowers()
            elif choice == '8':
                library.save_data()
                print("Data saved. Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
                
        except KeyboardInterrupt:
            print("\nProgram interrupted.")
            choice = input("Save before exiting? (y/n): ")
            if choice.lower() == 'y':
                library.save_data()
            print("Exiting program. Goodbye!")
            break
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()