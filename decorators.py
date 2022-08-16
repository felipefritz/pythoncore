

# a(b) -> c

def function_a(function_b): # global

    def function_c(*args, **kwargs): # local ambient
        print("before...")
        function_b(*args, **kwargs)
        print("after...")
    return function_c


@function_a
def sum(a, b):
    return print(a + b)


def my_decorator_name(name):
    def my_custome_decorator(function):
        def wrapper(*args, **kwargs):

            print('Name:', name)
            return function(*args, **kwargs)

        return wrapper

    return my_custome_decorator


@function_a
def suma(a, b):
    return print(a + b)

sum(10, 23)
suma(10, 20)