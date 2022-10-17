def calculator(operation, a, b):
    operations = {
        '+': lambda: a + b,
        '-': lambda: a - b,
        '*': lambda: a * b,
        '/': lambda: a / b
    }
    return operations.get(operation, lambda: None)()

print(calculator('+', 1000, 100))


# unpack operators: * and **
# ** unpack values of a dict. It cant' be used with list or tuple
# * unpack the keys of a dict and can be used with other datatypes
def function(*args, **kwargs):
    print('args', args)
    print(kwargs)


# use *
l = [1, 2, 3, 4, 5]
# use *
t = (6, 7, 8, 9, 10)
d = {'a': 1, 'b': 2}
# this use *
function(d, l , t, '2', 324)
# this use * and it will separate the string by char
function(*d, *l , *t, *'2', *'abckdfwdf')
# this use **
function(**d)

# map with lambda and list comprenhension: get  odd numbers
print('odd numbers,', list(map(lambda x: x * 1, [y for y in range(1, 50+1) if y % 2 == 1])))
# even numbers
print('even numbers,', list(map(lambda x: x * 1, [y for y in range(1, 50+1) if y % 2 == 0])))



