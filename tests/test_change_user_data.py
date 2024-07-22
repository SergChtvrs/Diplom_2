import requests
import allure
import pytest
from data import Endpoints, ResponseTexts


class TestChangeUserData:
    @allure.title('Данные авторизированного пользователя обновлены успешно')
    @pytest.mark.parametrize('user_attr, value',
                             [
                                 ["email", 'get_user_email'],
                                 ["name", 'get_user_password']
                             ], ids=['обновление email',
                                     'обновление пароля']
                             )
    def test_update_user_data_with_authorization_successful(self, request, registered_user, value, user_attr):
        param_value = request.getfixturevalue(value)
        payload = {
            user_attr: param_value
        }
        response = requests.patch(Endpoints.USER_ENDPOINT,
                                  headers={'Authorization': registered_user.access_token}, data=payload)
        assert response.status_code == 200 and param_value in response.text

    @allure.title('Данные пользователя не обновляются, если пользователь не авторизован')
    @pytest.mark.parametrize('user_attr, value',
                             [
                                 ["email", 'get_user_email'],
                                 ["name", 'get_user_password']
                             ], ids=['обновление email',
                                     'обновление пароля']
                             )
    def test_update_user_data_without_authorization_unsuccessful(self, request, value, user_attr):
        param_value = request.getfixturevalue(value)
        payload = {
            user_attr: param_value
        }
        response = requests.patch(Endpoints.USER_ENDPOINT, data=payload)
        assert response.status_code == 401 and response.text == ResponseTexts.UPDATE_USER_DATA_WITHOUT_AUTHORIZATION
