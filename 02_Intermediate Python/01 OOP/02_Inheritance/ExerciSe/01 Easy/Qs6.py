"""
Create a class `Vehicle` with a method `start()`.
Derive a class `Car` from `Vehicle` with its own method `stop()`.
"""
class Vehicle:
    def start(self):
        print('Start')

class Car(Vehicle):
    def stop(self):
        print("Car is stopped")

C1 = Car()
C1.start()
C1.stop()