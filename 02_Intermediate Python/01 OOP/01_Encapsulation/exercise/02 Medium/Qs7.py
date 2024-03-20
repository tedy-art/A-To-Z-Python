"""
Question 7:
Implement a SchoolClass class with private attributes
__students (a list of student names)
and
__teacher (the name of the teacher).
Provide methods to add a student, remove a student, and change the teacher.
"""


class SchoolClass:
    def __init__(self):
        self.__students = []
        self.__teacher = None

    def add_student(self, student_name):
        """Add a student to the class."""
        self.__students.append(student_name)

    def remove_student(self, student_name):
        """Remove a student from the class."""
        if student_name in self.__students:
            self.__students.remove(student_name)
        else:
            print('Student not found.')

    def change_teacher(self, new_teacher):
        """Change the teacher of the class."""
        self.__teacher = new_teacher

    # Getter methods to access private attributes (optional)
    def get_students(self):
        return self.__students

    def get_teacher(self):
        return self.__teacher


# Example usage:
school_class = SchoolClass()

# Add students
school_class.add_student("Student1")
school_class.add_student("Student2")
school_class.add_student("Student3")

# Remove a student
school_class.remove_student("Student2")

# Change teacher
school_class.change_teacher("New Teacher")

# Print students and teacher
print("Students:", school_class.get_students())
print("Teacher:", school_class.get_teacher())
