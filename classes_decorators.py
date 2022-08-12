"""
@property decorator
The @property decorator is a built-in decorator in Python for the property() function.
 Use @property decorator on any method in the class to use the method as a property.
You can use the following three decorators to define a property:

@property: Declares the method as a property.
@<property-name>.setter: Specifies the setter method for a property that sets the value to a property.
@<property-name>.deleter: Specifies the delete method as a property that deletes a property.


@classmethod (cls)
In Python, the @classmethod decorator is used to declare a method in the class as a class
method that can be called using ClassName.MethodName(). The class method can also be
called using an object of the class.

The @classmethod is an alternative of the classmethod() function.
It is recommended to use the @classmethod decorator instead
 of the function because it is just a syntactic sugar.
Declares a class method.
The first parameter must be cls, which can be used to access class attributes.
The class method can only access the class attributes but not the instance attributes.
The class method can be called using ClassName.MethodName() and also using object.
It can return an object of the class.

The class method can only access class attributes, but not the instance attributes.
 It will raise an error if trying to access the instance attribute in the class method.


@staticmethod:
The @staticmethod is a built-in decorator that defines a static method in the class in Python.
A static method doesn't receive any reference argument whether it is called by an instance
of a class or by the class itself.

Declares a static method in the class.
It cannot have cls or self parameter.
The static method cannot access the class attributes or the instance attributes.
The static method can be called using ClassName.MethodName() and also using object.MethodName().
It can return an object of the class.

The reason to use staticmethod is if you have something that
could be written as a standalone function (not part of any class),
but you want to keep it within the class because it's somehow semantically
related to the class. (For instance, it could be a function
that doesn't require any information from the class, but whose behavior
is specific to the class, so that subclasses might want to override it.)
In many cases, it could make just as much sense to write something as a
standalone function instead of a staticmethod.


"""


# @property example
class Student:
    def __init__(self, name):
        # __name will not available outside of the class without the @property decorator
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter  # property-name.setter decorator
    def name(self, value):
        self.__name = value\

    @name.deleter  # property-name.deleter decorator
    def name(self):
        print(f'Deleting {self.__name} ...')
        del self.__name


# @classmethod example
class Teacher:
    class_attribute = 'This is a class attribute'

    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age  # instance attribute

    @classmethod
    def getobject(cls):
        return cls('Bob', 30)

    @classmethod
    def tostring(cls):
        return cls.class_attribute


#@staticmethod example
class Person:
    name = 'unknown'  # class attribute

    def __init__(self):
        self.age = 20  # instance attribute

    @staticmethod
    def tostring():
        # It is possible to access to the class attributes
        person = Person.name = 'Steve'
        print('Person Class', person)


if __name__ == "__main__":
    student = Student('Steve')

    #@property applied here
    print(student.name)

    # @setter applied here:
    student.name = 'Bill'

    # @property deleter applied here:
    del student.name
    print('attribute name deleted', student)

    # classmethod
    teacher = Teacher.getobject()
    print('classmehod  example, getobject: ', teacher.name)
    print('classmethod example, tostring: ', teacher.tostring())

    # @staticmethod example
    print(Person.tostring())