from abc import ABC, abstractmethod

# with python, the abstrac class should receive ABC
# must have at least one abstract method


class Personaje(ABC):
    @abstractmethod
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 0

    @abstractmethod
    def atack(self, objective):
        """pass because this will be overwrite
        in subclasses, but it can have code
        """
        pass