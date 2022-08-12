
from collections import Counter, namedtuple, defaultdict, deque


# Count
test_var= [1, 2, 3, 5, 5, 'hello', 'test', 'test', 'test']
def count_most_common_in_object(object):
    count_most_common = Counter(object).most_common(2)
    print(count_most_common)
    return count_most_common[0][0]

count_most_common_in_object(test_var)
#namedtuple
def build_coordinates_object(x: float, y: float):
    Coordinate = namedtuple('Coordinate', 'x,y')
    coordinates = Coordinate(x, y)
    return coordinates

# Ordereddict: es un diccionario el cual recuerda el orden en que fueron insertados los elementos
# defaultdict: se le pasa un valor predeterminado para que devuelva un valor en vez de keyerror
dictionary = defaultdict(str)
dictionary['a'] = 'test'
print(dictionary['a'])


# deque: it allow to manage with a best way the lists
q = deque()
for i in range(3):
    q.append(i)
q.appendleft(3)
#q.popleft() # removes the left item
#q.clear() # clean all the elements
q.extend([5,6,7, 'test'])
# extends the deque, also it could be used with extendsleft
q.rotate(2) # This will rotate the last items to the first places
print(q)
