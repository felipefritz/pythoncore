"""
protege métodos o atributos de otras clases
o desde el exterior. Para acceder a estos
métodos o atributos se utilizan métodos de
acceso para que se pueda a acceder desde afuera
de la clase
"""


class Car:
    # here can be the initial attributes, but is necesary to
    # use it with the constructor
    # large= 100
    # width = 120
    # wheels = 4
    # is_moving = False

    # constructor or initial state for all objects of this class
    # the constructor specify the initial state of the objects

    def __init__(self):
        self.large = 100
        self.width = 120
        self.__is_moving = False

        # in python encapsulation or make private
        # an attribute or method there is to use __
        # Encapsulation for this attribute

        self.__wheels = 4

    def __internal_check(self):
        # this is a privated method or encapsulated
        print("checking car done")
        return True

    def move(self):
        # Use of private method inside the class
        self.__internal_check()
        self.__is_moving = True

    def state(self):
        print(self.__wheels)
        print(self.width)
        print(self.__is_moving)

    def change_wheels(self, wheels_number):
        # this function change a private attribute
        self.__wheels = wheels_number


my_car = Car()

"""encapsulation example:"""

# private : it can't be modified from out of the class
my_car.__wheels = 2
# public: can me modified from outside of the class
my_car.width = 200
my_car.state()

my_car.change_wheels(10)
my_car.state()

my_car.move()
my_car.state()

# this method can't be accessed from outside
my_car.__internal_check()

