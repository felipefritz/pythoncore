import requests
from logs.loggers import Logger, logging
from abc import ABC, abstractmethod


class HttpClient(ABC):

    def __init__(self, base_url):
        self.base_url = base_url

    @abstractmethod
    def get(self, endpoint):
        pass


class RestClient(HttpClient):
    def get(self, endpoint):
        try:
            response = requests.get(url=self.base_url + endpoint)
            Logger('info', f' info fetched success from api', logger_name=logging.getLogger(__name__))
            return response

        except Exception as e:
            Logger('error', e, logger_name=logging.getLogger(__name__))


class Address:
    def __init__(self, street, suite, city, zipcode, lat, lng):
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.geo = self.Geo(lat, lng)

    def __str__(self):
        return f'{self.street}'

    class Geo:
        def __init__(self, lat, lng):
            self.lat = lat
            self.lng = lng

        def __str__(self):
            return f'{self.lat}, {self.lng}'


class User:

    def __init__(self, id, name, username, email, address: Address):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.address = address

    def __str__(self):
        return f'{self.name}'
# f f

if __name__ == '__main__':
    users = set()
    jsonplaceholder_client = RestClient(base_url='https://jsonplaceholder.typicode.com')
    users_from_api = jsonplaceholder_client.get(endpoint='/users').json()

    for u in users_from_api:
        user_address = Address(city=u['address']['city'],
                               street=u['address']['street'],
                               suite=u['address']['suite'],
                               zipcode=u['address']['zipcode'],
                               lat=u['address']['geo']['lat'],
                               lng=u['address']['geo']['lng'])
        user = User(id=u['id'],
                    name=u['name'],
                    username=u['username'],
                    email=u['email'],
                    address=user_address)
        users.add(user)
    print(users)
