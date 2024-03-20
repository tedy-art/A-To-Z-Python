class P:
    def m1(self):
        print("This is parent m1 method")


class c(P):
    def m2(self):
        print("This is child m2 method")


jay = c()
jay.m2()
jay.m1()
