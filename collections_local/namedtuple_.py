from collections import namedtuple


def build_coordinates_object(x: float, y: float):
    Coordinate = namedtuple('Coordinate', 'x,y')
    coordinates = Coordinate(x, y)
    return coordinates


def create_object(object_name, attributes):
    return namedtuple(object_name, attributes)



