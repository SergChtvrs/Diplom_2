import requests
import allure
import pytest
from data import Endpoints, WrongUserData, ResponseTexts


class TestLoginUser:
    @allure.title('Авторизация зарегистрированного пользователя успешна')
    def test_registered_user_login_successful(self, registered_user):
        payload = {
            "email": registered_user.email,
            "password": registered_user.password
        }
        response = requests.post(Endpoints.USER_LOGIN_ENDPOINT, data=payload)
        assert response.status_code == 200 and '"success":true' in response.text

    @allure.title('Пользователь не авторизован, если email или пароль некорректны')
    @pytest.mark.parametrize('wrong_param, invalid_value',
                             [
                                 ["'email'", WrongUserData.WRONG_EMAIL],
                                 ["'password'", WrongUserData.WRONG_PASSWORD]
                             ], ids=['некорректный email пользователя',
                                     'некорректный пароль пользователя']
                             )
    def test_user_login_with_wrong_params_unsuccessful(self, registered_user, wrong_param, invalid_value):
        if wrong_param == 'email':
            payload = {
                "email": invalid_value,
                "password": registered_user.password
            }
        else:
            payload = {
                "email": registered_user.email,
                "password": invalid_value
            }

        response = requests.post(Endpoints.USER_LOGIN_ENDPOINT, data=payload)
        assert response.status_code == 401 and response.text == ResponseTexts.USER_LOGIN_WITH_WRONG_PARAMS
