"""
__add__:  +
__sub__ para -
__len__ para len()

__mul__ para *
__str__ return string object representation
__truediv__ para /
floordiv para //
__mod__ para %
__pow__ para **
__and__ para &
__or__ para |
__it__ para <
__le__ para <=
__eq__ para ==
__ne__ para !=
__gt__ para >
__ge__ para >=
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

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

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


if __name__ == '__main__':
    # __add__
    object1 = Vector2D(5, 7)
    object2 = Vector2D(3.23, 9)
    object3 = Vector2D(3, 83)
    result = object1 - object2 - object3
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


