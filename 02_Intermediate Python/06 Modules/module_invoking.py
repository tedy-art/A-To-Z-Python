import mymodule
import mymodule1
from mymodule2 import person

print(mymodule.greeting("Tejas"))
a = mymodule1.person["name"]
b = mymodule1.person["age"]
print(a)
print(b)

print(person["age"])
