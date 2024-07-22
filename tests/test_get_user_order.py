import requests
import allure
from helpers import make_order
from data import Endpoints, ResponseTexts


class TestGetUserOrder:
    @allure.title('Успешное получение заказов пользователя с авторизацией')
    def test_get_authorized_user_orders_successful(self, registered_user):
        user_order = make_order(registered_user)

        response = requests.get(Endpoints.ORDER_ENDPOINT, headers={'Authorization': registered_user.access_token})
        assert response.status_code == 200 and response.json()['orders'][0]['number'] == user_order

    @allure.title('Ошибка при получении заказов пользователя без авторизации')
    def test_get_unauthorized_user_orders_unsuccessful(self):
        response = requests.get(Endpoints.ORDER_ENDPOINT)
        assert response.status_code == 401 and response.text == ResponseTexts.GET_UNAUTHORIZED_USER_ORDERS
