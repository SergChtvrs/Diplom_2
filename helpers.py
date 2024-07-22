import random
import secrets
import string
import requests
from data import User, Endpoints


def email_generator():
    name = "mark"
    domain = "@yandex.ru"
    email = name + str(random.randint(1000, 9999)) + domain
    return email


def password_generator():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(6))
    return password


def user_attr_to_dict_converter(user):
    user_data = vars(user)
    return user_data


def create_user_data():
    email = email_generator()
    password = password_generator()
    user = User(email, password)
    return user


def delete_user(user):
    response = requests.delete(Endpoints.USER_ENDPOINT, headers={'Authorization': user.access_token})
    if response.status_code != 202:
        raise Error("Пользователь не удален")


def register_user():
    user = create_user_data()
    payload = user_attr_to_dict_converter(user)
    response = requests.post(Endpoints.REGISTER_ENDPOINT, data=payload)
    if response.status_code == 200:
        user.access_token = response.json()["accessToken"]
    else:
        raise Error("Пользователь не зарегистрирован")
    return user


def create_burger():
    burger = []
    burger_types = ['bun', 'main', 'sauce']
    response = requests.get(Endpoints.INGREDIENTS_ENDPOINT)
    if response.status_code == 200:
        for types in burger_types:
            for ingredients in response.json()['data']:
                if ingredients['type'] == types:
                    burger.append(ingredients['_id'])
                    break
    else:
        raise Error("response.status_code != 200")
    return burger


def make_order(user):
    burger = create_burger()
    payload = {
        "ingredients": burger
    }

    response = requests.post(Endpoints.ORDER_ENDPOINT,
                             headers={'Authorization': user.access_token}, data=payload)
    if response.status_code == 200:
        return response.json()['order']['number']
    else:
        raise Error("Заказ не создан")


class Error(Exception):
    pass
