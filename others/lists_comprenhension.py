multiples = [i for i in range(0, 501)
             if i%2 == 0
             and i%3 == 0
             and i%4 == 0
             and i%8 == 0]

# list to dict
# method 1:
# dict.fromkeys(list, defaultValue)
fruits = ["Apple", "Pear", "Peach", "Banana"]
fruit_dictionary = dict.fromkeys(fruits, "")
# method 2:
fruit_dictionary_m2 = { fruit : 0 for fruit in fruits }

print(fruit_dictionary)
print(fruit_dictionary_m2)


# list comprenhension with decorator
def convert_list_to_dict(function):
    def wrappper(*args, **kwargs):
        l = function(*args, **kwargs)
        return dict.fromkeys(l, '')
    return wrappper


@convert_list_to_dict
def list_generator(q: int):
    return [f'object_{i}' for i in range(q)]

print(list_generator(10))