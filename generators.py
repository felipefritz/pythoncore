
# Is used for create iterations and return a serie of iterable elements
# are  more slow than list comprehension but it can improve the memory usage
# is used with yield in functions.
import requests
from collections import namedtuple


def insert_to_db(product):
    print(f'product {product.title} inserted success to the database!' )


def get_product():
    products = requests.get(url='https://dummyjson.com/products').json()['products']
    for producto in products:
        yield producto
pr = get_product()

print(next(pr))

for product in get_product():
    Object = namedtuple('product', product)
    p = Object(**product)
    insert_to_db(p)