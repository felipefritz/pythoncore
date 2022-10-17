"""
Are functions stored in variables and can be passed to
a function as variables

Excercice:
create a function that can find an string in a list of
dicts.
it is necesary to use first class functions
"""


persons = [
    {"name": "Bob", "age": 23},
    {"name": "Steve", "age": 30},
    {"name": "Elliot", "age": 20},
]


def search_element(sequence, result, finder):
    return [element for element in sequence if finder(element) == result][0]


def search_person_name(person):
    return person["name"]


print(search_element(persons, "Bob", search_person_name))