"""
Create a product class
 with 3 class that inheritc from product
"""


class Product:
    def __init__(self, name, description, code):
        self.description = description
        self.name = name
        self.code = code

    def __str__(self):
        return f"{self.code} {self. name} {self.description}"


class Aliment(Product):
    brand = ""
    distribuitor = ""

    def __str__(self):
        return f"{super().__str__()}, brand: {self.brand}, " \
               f"dist:  {self.distribuitor}"


al = Aliment(name="pop corns", description="corn", code="23")
al.brand = "test"
al.distribuitor = "DISTI"
print(al)