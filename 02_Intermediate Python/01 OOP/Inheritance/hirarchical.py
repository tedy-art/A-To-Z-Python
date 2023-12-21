class p:
    def m1(self):
        print("This is parent m1 method.")

class c1(p):
    def m2(self):
        print("This is child1 m2 method.")


class c2(p):
    def m3(self):
        print("This is child2 m3 method.")

jay = c1()
jay.m2()
jay.m1()

viru = c2()
viru.m1()
viru.m3()