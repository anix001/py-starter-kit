# Inheritance= Allows  a class inherit attribute and methods from another class
# Helps with code reusability and extensibility

# class Animal:

#     def __init__(self, name):
#         self.name  = name
#         self.is_alive = True

#     def  eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")


# class Dog(Animal):
#   pass

# dog = Dog("dog1")

# print(dog.is_alive)


# Multiple Inheritance = inherit from more than  one parent class
#    C (A, B)

# class Prey:
#     def flee(self):
#         print("This animal is fleeting")

# class Predator:
#     def hunt(self):
#      print("This animal is hunting")

# class Fish(Prey, Predator):
#    pass

# fish = Fish()

# fish.flee()
# fish.hunt()


# MultiLevel Inheritance = inherit from  a parent which inherit from another parent
# C(B) -> B(A)-> A 

# class A:
#     def funcA(self):
#         print("From class A")

# class B(A):
#     def funcB(self):
#         print("From class B")
    
# class C(B):
#     def funcC(self):
#         print("From class C")

# test = C()
# test.funcA()
# test.funcB()
# test.funcC()


# Super() = Function used in a child  to call methods from a parent class (superclass)
# Allows you to extend the functionality of inherited methods

class Shape:
   def __init__(self, color, is_filled):
      self.color = color
      self.is_filled = is_filled

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
      super().__init__(color, is_filled)
      self.radius = radius

circle = Circle("red", True , 3.5)

print(circle.color)
    
