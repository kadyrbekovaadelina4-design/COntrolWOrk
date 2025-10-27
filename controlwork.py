class Person:
    def __init__(self, age):
       self.__age = age
    def set_age (self,age):
       if age >= 15:
           self.__age = age
       else:
           return ("Ошибка: возрост не может быть отрицательным")

   def get_age(self):

       return self.__age

class  Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return "I am an Animal"
class Dog(Animal):


   def speak(self):
        return "Woof"

class Cat(Animal):
   def speak(self):
       return "Meow"


class Vehicle:
   def move(self):
       return "Vehicle is moving"

class Car(Vehicle):
   def move(self):
        return "Car is driving"

   class Bicycle(Vehicle):
       def move(self):

           return "Bicycle is pedaling"

   def move(vehicle):

       return vehicle.move()



import math

class Shape:
    def area(self):
        raise NotImplementedError("Этот метод должен быть переопределен в классах-наследниках.")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


rect = Rectangle(10, 5)
circle = Circle(7)

print(f"Площадь прямоугольника: {rect.area()}")
print(f"Площадь круга: {circle.area():.2f}")


try:
    s = Shape()
    s.area()
except NotImplementedError as e:
    print(f"\nОшибка: {e}")