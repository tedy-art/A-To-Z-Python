"""
Question 4:
Create a class Student with private attributes name and age.
Include a method to display the student's information.
"""


class Student:
    def __init__(self):
        self.__name = None
        self.__age = None

    def set_info(self, name, age):
        self.__name = name
        self.__age = age

    def get_info(self):
        print(f"student name is `{self.__name}` and age `{self.__age}`.")


student_instance = Student()
student_instance.set_info('Tejas', 26)
student_instance.get_info()
