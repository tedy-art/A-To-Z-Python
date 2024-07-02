"""
Define a class Vehicle with a method drive().
Create a class Car inheriting from Vehicle with its own method park().
"""


class Vehicle:
    def drive(self):
        return f"Vehicle is running..."


class Car(Vehicle):
    def park(self):
        return f"car is parked"


nano = Car()
print(nano.drive())
print(nano.park())
