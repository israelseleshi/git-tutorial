# **************************************************
# LIBRARY MANAGEMENT SYSTEM
# **************************************************

# **************************************************
class Book:
# **************************************************
  
  # CONSTRUCTOR
  def __init__(self, title, author, isbn):
    self.title = title
    self.author = author
    self.isbn = isbn
    self.available = True

  # STRING REPRESENTATION
  def __str__(self):
    return f"Book(Title = {self.title},\
             Author = {self.author},\
             ISBN = {self.isbn},\
             Available = {self.available})"
# **************************************************





# **************************************************
class Patron:
# **************************************************

  # CONSTRUCTOR
  def __init__(self, name, library_card_number):
    self.name = name
    self.library_card_number = library_card_number
    self.checked_out_books = []


  # STRING REPRESENTATION
  def __str__(self):
    return f"Patron(Name = {self.name}, Library Card Number = {self.library_card_number})"


  # check_out_book method
  def check_out_book(self, book):
    
    if book.available:
      book.available = False
      self.checked_out_books.append(book)
      return f"{book.title} has been checked out to {self.name}."
    else:
      return f"{book.title} is not available."


  # check_out_book method
  def return_book(self, book):
    
    if book in self.checked_out_books:
      book.available = True
      self.checked_out_books.remove(book)
      return f"{book.title} has been returned by {self.name}"
    else:
      return f"{self.name} does not have {book.title} checked out."

  
# **************************************************
    




# **************************************************
class Library:
# **************************************************
  
  # CONSTRUCTOR
  def __init__(self):
    self.books = []
    self.patrons = []


  # STRING REPRESENTATION
  def __str__(self):
    return f"Books = {[self.books]}\nPatrons = {[self.patrons]}"


  # add_book method
  def add_book(self, book):

    self.books.append(book)
    return f"{book.title} has been added to the library!"
  

  # add_patron method
  def add_patron(self,patron):

    self.patrons.append(patron)
    return f"{patron.name} has been added to the library!"


  # find_book_by_isbn method
  def find_book_by_isbn(self, isbn):
    
    for book in self.books:
      if book.isbn == isbn:
        return book
    return None


  # find_patron_by_card_number method
  def find_patron_by_card_number(self, card_number):
    
    for patron in self.patrons:
      if patron.library_card_number == card_number:
        return patron
    return None


  # list_available_books method
  def list_available_books(self):
    return [book for book in self.books if book.available]


  # list_checked_out_books method
  def list_checked_out_books(self):
    return [book for book in self.books if not book.available]    

# **************************************************


# **************************************************
def main():
# **************************************************

  library = Library()

  # Initializing Books
  Atomic_Habits = Book("Atomic Habits", "James Clear" ,"12345678")
  Eat_That_Frog = Book("Eat That Frog", "Brian Tracy" ,"87654321")

  # Initializing Patrons
  Patron1 = Patron("Israel Theodros", 12345)
  Patron2 = Patron("Theodros Seleshi", 54321)

  # Adding Books
  library.add_book(Atomic_Habits)
  library.add_book(Eat_That_Frog)

  # Adding Patrons
  library.add_patron(Patron1)
  library.add_patron(Patron2)

  while True:
    print()
    print("="*32)
    print("📖 Library Management System 📖")
    print("1. Add a Book")
    print("2. Add a Patron")
    print("3. Check Out Book")
    print("4. Return Book")
    print("5. List Available Books")
    print("6. List Checked Out Books")
    print("7. Exit")
    print("="*32)

    print()
    choice = int(input("🔢 Enter your choice: "))


    # add a book
    if choice == 1:

      print()
      print("="*32)
      print("➕📕 Add Book ➕📕".center(32))
      print("="*32)

      title  = input("Enter book title: ")
      author = input("Enter book author: ")
      isbn   = input("Enter book isbn: ")

      book   = Book(title, author, isbn)
      print(library.add_book(book))


    # add a patron
    elif choice == 2:

      print()
      print("="*32)
      print("➕😎 Add Patron ➕😎".center(32))
      print("="*32)

      name  = input("Enter patron name: ")
      library_card_number = int(input("Enter library card number: "))

      patron   = Patron(name, library_card_number)
      print(library.add_patron(patron))

    
    # check_out_book
    elif choice == 3:

      print()
      print("="*32)
      print("➖📕 Check Out Book ➖📕".center(32))
      print("="*32)

      isbn = input("Enter book ISBN to check out: ")
      card_number = int(input("Enter patron library card number: "))

      book = library.find_book_by_isbn(isbn)
      patron = library.find_patron_by_card_number(card_number)
    
      if book and patron:
        print(patron.check_out_book(book))
      else:
        print("Invalid book ISBN or patron card number!")


    # return book
    elif choice == 4:
      
      isbn = input("Enter book ISBN to return: ")
      card_number = int(input("Enter patron library card_number: "))

      book = library.find_book_by_isbn(isbn)
      patron = library.find_patron_by_card_number(card_number)

      if book and patron:
        print(patron.return_book(book))
      else:
        print("Invalid book ISBN or patron card number.")
    

    # list available books
    elif choice == 5:
      print("\nAvailable Books: ")
      for book in library.list_available_books():
        print(book)
    

    # list checked out books
    elif choice == 6:
      print("\nChecked Out Books: ")
      for book in library.list_checked_out_books():
        print(book)


    # exit
    elif choice == 7:
      break

    else:
      print("Invalid choice. Please try again!")

# **************************************************

if __name__ == "__main__":
  main()