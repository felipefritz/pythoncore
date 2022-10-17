from collections import defaultdict

""" Ordereddict: es un diccionario el cual recuerda el orden en que fueron insertados los elementos
defaultdict: se le pasa un valor predeterminado para que devuelva un valor en vez de keyerror

If your code is heavily base on dictionaries and you’re dealing with missing keys all the time,
 then you should consider using a defaultdict rather than a regular dict.

If your dictionary items need to be initialized with a constant default value, 
then you should consider using a defaultdict instead of a dict.

If your code relies on dictionaries for aggregating, accumulating, 
counting, or grouping values, and performance is a concern, then you should consider using a defaultdict.

"""

"""Grouping data"""

d = [('Sales', 'John Doe'),
     ('Sales', 'Martin Smith'),
     ('Accounting', 'Jane Doe'),
     ('Marketing', 'Elizabeth Smith'),
     ('Marketing', 'Elizabeth Smith'),
     ('Marketing', 'Adam Doe'),
     ('Marketing', 'Adam Doe'),
     ('Marketing', 'Adam Doe')]


def group_items_by_name(l: []):
    results = defaultdict(list)
    for name, item in l:
        results[name].append(item)
    return results


def group_unique_items(l: []):
    results = defaultdict(set)
    for name, value in l:
        results[name].add(value)
    return results


# Count items
def count_items_by_name(l: []):
    dd = defaultdict(int)
    for name, _ in l:
        dd[name] += 1
    return dd


a = group_unique_items(d)
print(a)
