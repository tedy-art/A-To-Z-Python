class GP:
    def m3(self):
        print("This is Grand parent m3 method.")

class P(GP):
    def m1(self):
        print("This is paranet m1 method.")

class c(P):
    def m2(self):
        print("This is child m2 method")


jay = c()
jay.m2()
jay.m1()
jay.m3()