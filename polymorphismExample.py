# Polymorphism = Many Form

# Two Ways to achieve this
# 1. Inheritance
# 2. Duck Typing = Object must have minimum necessary attributes/methods
#                 If it looks like a duck and quack like a duck then it must be duck


class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof !!")

class Cat(Animal):
    def speak(self):
        print("Meow !!")

class Car:
    alive= False
    
    # Instance_method
    def speak(self):
        print("Honk!!")

animals = [Dog(), Cat(), Car()]


for animal in animals:
    animal.speak()
    print(animal.alive)

# If car has minm attribute to be consider animal, it should be considered as animal(that's what duck typing mean)
