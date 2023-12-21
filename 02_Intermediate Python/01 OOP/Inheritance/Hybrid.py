class school:
    def func1(self):
        print("This function is in school.")

class student1(school):
    def func2(self):
        print("This function is in student1.")

class student2(school):
    def func3(self):
        print("This function is in student2.")

class student3(student1, school):
    def func4(self):
        print("This function is in student3.")

print('*'*10, "student3", '*'*10)
o1 = student3()
o1.func1()
o1.func2()
o1.func4()

print('*'*10, "student2", '*'*10)
o2 = student2()
o2.func1()
o2.func3()

print('*'*10, "student1", '*'*10)
o3 = student1()
o3.func1()
o3.func2()

print('*'*10, "School", '*'*10)
o4 = school()
o4.func1()