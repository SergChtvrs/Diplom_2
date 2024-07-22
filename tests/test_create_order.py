import requests
import allure
from data import Endpoints, ExpectedResults, ResponseTexts


class TestCreateOrder:
    @allure.title('Создание заказа с авторизацией успешно')
    def test_create_order_with_authorization(self, registered_user, ingredient_options):
        ingredients, expected_result = ingredient_options
        payload = {
            "ingredients": ingredients
        }

        response = requests.post(Endpoints.ORDER_ENDPOINT,
                                 headers={'Authorization': registered_user.access_token}, data=payload)

        if expected_result == ExpectedResults.CREATE_ORDER_WITH_CORRECT_INGREDIENTS:
            assert (response.status_code == expected_result and
                    response.json()['order']['owner']['email'] == registered_user.email and
                    response.json()['order']['ingredients'][1]['_id'] in ingredients)
        if expected_result == ExpectedResults.CREATE_ORDER_WITH_WRONG_INGREDIENTS:
            assert response.status_code == expected_result
        if expected_result == ExpectedResults.CREATE_ORDER_WITHOUT_INGREDIENTS:
            assert (response.status_code == expected_result and
                    response.text == ResponseTexts.CREATE_ORDER_WITHOUT_INGREDIENTS)

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_authorization(self, ingredient_options):
        ingredients, expected_result = ingredient_options
        payload = {
            "ingredients": ingredients
        }

        response = requests.post(Endpoints.ORDER_ENDPOINT, data=payload)

        if expected_result == ExpectedResults.CREATE_ORDER_WITH_CORRECT_INGREDIENTS:
            assert (response.status_code == expected_result and
                    '"success":true' in response.text)
        if expected_result == ExpectedResults.CREATE_ORDER_WITH_WRONG_INGREDIENTS:
            assert response.status_code == expected_result
        if expected_result == ExpectedResults.CREATE_ORDER_WITHOUT_INGREDIENTS:
            assert (response.status_code == expected_result and
                    response.text == ResponseTexts.CREATE_ORDER_WITHOUT_INGREDIENTS)
