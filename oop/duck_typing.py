# Two classes with a same function that calls equal
class Dog:
    def move(self):
        print("I am walking...")


class Shark:
    def move(self):
        print("I am swimming...")


# a class that does not share the method move
class Vehicle:
    def avanzar(self):
        print("driving...")


# this class works with any class that has move
# because dog and shark  are Animals
# and all have the same method
class Animal:
    def __init__(self, animal):
        self.animal = animal
        self.animal.move()

    def action(self):
        self.animal.move()






