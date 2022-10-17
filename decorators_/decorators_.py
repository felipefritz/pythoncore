from decorators_.decorators import print_results, login, make_secure


@print_results
def hello_world(a, b):
    return "hello with a decorator"


@login(access_level="admin")
def get_user_info(user_id):
    user = [u for u in users if user_id == u["id"]]
    return user if user else False


@make_secure
def get_admin_password():
    return "1234"


@make_secure
def get_designer_password():
    return "4321"


if __name__ == '__main__':
    user = {"id": 1, "access_level": "admin"}
    users = [
        {"id": 1, "name": "bob", "access_level": "admin"},
        {"id": 2, "name": "steve", "access_level": "dev"},
        {"id": 3, "name": "elliot", "access_level": "editor"},

    ]

    hello_world()

    print(get_user_info(20))
    # This will return the name of the function using functools:
    print(get_user_info.__name__)
    print(get_admin_password(user))
