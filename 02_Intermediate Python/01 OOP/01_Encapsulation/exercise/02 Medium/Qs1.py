"""
Question 1:
Implement a Library class with private attributes __books (a list of book titles)
and __members (a list of member names). Provide methods to add a book,
remove a book, add a member, and remove a member.

class Library -
        1) attributes:
            1) __books(a list of book titles)
            2) __member(a list of member names)
        2) methods:
            1)book(on book method)
                1) add a book
                2) remove a book
            2)member(on member method)
                1) add a member
                2) remove a member

"""


class Library:
    def __init__(self):
        self.__books = []
        self.__members = []

    def add_book(self, book_title):
        self.__books.append(book_title)
        print(f"Book '{book_title}' add to the library")

    def remove_book(self, book_title):
        if book_title in self.__books:
            self.__books.remove(book_title)
        else:
            print(f"book '{book_title}' is not fond in library.")

    def add_member(self, member_title):
        self.__members.append(member_title)
        print(f"Member '{member_title}' add to the library")

    def remove_member(self, member_title):
        if member_title in self.__members:
            self.__members.remove(member_title)
            print(f"Member '{member_title}' removed from the library.")
        else:
            print(f"Member '{member_title}' is not fond in library.")

    def display_library_info(self):
        print("Library Information : ")
        print("Book : ", self.__books)
        print("Members", self.__members)


library_instance = Library()

library_instance.add_book("The Great Gatsby")
library_instance.add_book("To kill a mockingbird")
library_instance.add_member("John Doe")
print("-----------------------------")


library_instance.display_library_info()
print("-----------------------------")

library_instance.remove_book("The Great Gatsby")
library_instance.remove_member("John Doe")
print("-----------------------------")

library_instance.display_library_info()
print("-----------------------------")
