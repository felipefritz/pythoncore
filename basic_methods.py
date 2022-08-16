# strings methods that returns boolean

#  string.isalnum() -> if is alphanumeric or not
# string .isdigit() -> if is numeric or not
# string.isalpha() -> only alphanumeric
# string.islower() -> if is lower
# string.isspace() -> if all char are space
# string.startswith() | endswith() -> is starts or ends with

# methods:
# string.split('value') -> return a list of strings
# ",".join('helloWorld') -> h,e,l,l,o,W,o,r,l,d
# string.strip('value' or empty) -> remove spaces at the end and start
# string.replace(value, newValue, num_of_items_to_replace)
# string.capitalize() -> first char uppercase
# string.title() -> first char in all words to uppercase
# string.count(value) -> count how many times is the value in string
 # string.find(value) -> return the position number



 # DEAULTDICTS:
  # si se accede a una llave que no existe,
  # este retornara siempre algo dependiendo
  # del tipo de dato que se declaro al iniciarlo


 # from collections import defaultdict
# d = defaultdict(float) -> dict with float  values


# ORDEREDDICTS:
    # son diccionarios ordenados
# from collections import OrderedDict


# NAMEDTUPLE:
# are tuples that can be used as objects
# are inmutable
 # from collections import namedtuple

 # Person = namedtuple('Person' , 'name lastname age')
 # p = Person(name='bob', lastname='test', age=25)
 # p.name -> bob