"""
Question 5:
Implement a class Book with private attributes title and author.
Provide methods to set and get book details.
"""


class Book:
    def __init__(self):
        self.__title = ""
        self.__author = ""

    def set_details(self, title, author):
        self.__title = title
        self.__author = author

    def get_details(self):
        print(f"Name of book is `{self.__title}` and it's author is `{self.__author}`.")


book_instance = Book()
book_instance.set_details("way to home", "Tejas")
book_instance.get_details()
