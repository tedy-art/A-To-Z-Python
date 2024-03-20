class p1:
    def m1(self):
        print("This is parent1 m1 method.")

class p2:
    def m2(self):
        print("This is parnet2 m2 method.")

class c(p1, p2):
    def m3(self):
        print("This is child m3 method.")

jay = c()
jay.m2()
jay.m1()
jay.m3()