import functools


def function_a(function_b): # global

    def function_c(*args, **kwargs): # local ambient
        print("before...")
        function_b(*args, **kwargs)
        print("after...")
    return function_c


def my_decorator_name(name):
    def my_custome_decorator(function):
        def wrapper(*args, **kwargs):

            print('Name:', name)
            return function(*args, **kwargs)

        return wrapper

    return my_custome_decorator


"""Example 2:
using functiontools.wraps allow to get the 
name of the external function, not the decorator internal
function.
example: 
secure_function: internal function
external function: decorated function (get_admin_password)
"""


def make_secure(func):
    @functools.wraps(func)
    def secure_function(user, *a, **k):
        if user == "admin":
            return func(a)
        else:
            return f'permission denied for user {user["id"]} '

    return secure_function


"""Decorator with arguments
create a login function with decorators
the decorator argument should be the user id
return: user data
"""


def login(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*a, **k):
            user = func(*a, **k)
            if not user:
                return "user does not exists"
            return "authorized!" if user[0]["access_level"] == access_level else "not authorized"
        return secure_function
    return decorator


def print_results(function):
    def wrapper(*args, **kwargs):

        print(function(args, kwargs))

    return wrapper








