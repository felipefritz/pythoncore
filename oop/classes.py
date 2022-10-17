"""
__add__:  +
__sub__ para -
__len__ para len()
__add__(self, other)	To get called on add operation using + operator
__sub__(self, other)	To get called on subtraction operation using - operator.
__mul__(self, other)	To get called on multiplication operation using * operator.
__floordiv__(self, other)	To get called on floor division operation using // operator.
__truediv__(self, other)	To get called on division operation using / operator.
__mod__(self, other)	To get called on modulo operation using % operator.
__pow__(self, other[, modulo])	To get called on calculating the power using ** operator.
__lt__(self, other)	To get called on comparison using < operator.
__le__(self, other)	To get called on comparison using <= operator.
__eq__(self, other)	To get called on comparison using == operator.
__ne__(self, other)	To get called on comparison using != operator.
__ge__(self, other)	To get called on comparison using >= operator.
__mul__ para *
__str__ return string object representation
__truediv__ para /
floordiv para //
__mod__ para %
__pow__ para **
__and__ para &
__or__ para |
__it__ para <
__getitem__ para indexar
__setitem__ para asignar valores indexados
__delitem__ para borrar valores indexados
__iter__ para iteración sobre objetos
__contains__ para in
"""


class Vector2D:
    def __init__(self, x, y, data: list = None):
        self.x = x
        self.y = y
        self.data = data

    def __str__(self):
        import traceback

        (filename, line_number, function_name, text) = traceback.extract_stack()[-2]
        def_name = text[:text.find('=')].strip()
        self.defined_name = def_name.replace('print(', '')
        return f'{self.defined_name}: {self.x, self.y}'

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __or__(self, other):
        if self.x > other.x and  self.y > other.y:
            return Vector2D(self.x, self.y)
        else:
            return Vector2D(other.x, other.y)

    def __len__(self):
        if self.data:
            return len(self.data)
        else:
            return 0

    def __getitem__(self, position):
        if self.data:
            return self.data[position]

    def __setitem__(self, key, value):
        if self.data:
            self.data[key] = value

    def __iter__(self):
        if self.data:
            for pos in range(0, len(self.data)):
                yield f"Value[{pos}]: {self.data[pos]}"


class Outside:
    def __init__(self):
        self.name = 'Outside object'
        self.inside = self.Inside()

    class Inside:
        def __init__(self):
            self.name = 'I am inside'


# duck typing example
class Truck:
    def start(self):
        print( 'truck starting...')

    def stop(self):
        print('truck stoping')


class Car:
    def start(self):
        print('car starting...')

    def stop(self):
        print('car stoping')


class Vehicle:
    def __init__(self, vehicle):
        self.vehicle = vehicle
        self.vehicle.start()
        self.vehicle.stop()

    def action(self):
        self.vehicle.start()
        self.vehicle.stop()


if __name__ == '__main__':
    # __add__
    object1 = Vector2D(5, 7)
    object2 = Vector2D(3.23, 9)
    object3 = Vector2D(3, 83)
    result = object1 + object2 + object3
    print('add:', result.x, result.y)

    object1.data = [1, 2, 3]

    # __getitem__
    print('getitem pos 0:', object1[0])

    # __setitem__
    object1[0] = 10
    print('setItem pos 0:', object1[0])

    # __len__
    print('len:', len(object1))

    # __iter__
    iter_object = iter(object1)
    print('iter:', next(iter_object))
    print('iter:', next(iter_object))
    print('iter:', next(iter_object))

    #other
    print(object1 | object2)

    print(object1)

    # Internal class Example:

    # outside = Outside()
    print('outside object class:', Outside().name)

    print('inside object class:', Outside().inside.name)


    # ducktyping:

    car = Vehicle(Car())
    truck = Vehicle(Truck())
    truck.action()
