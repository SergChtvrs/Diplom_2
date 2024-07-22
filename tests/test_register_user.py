import allure
import requests
import pytest
from data import Endpoints, ResponseTexts
from helpers import user_attr_to_dict_converter, create_user_data


class TestRegisterUser:
    @allure.title('Регистрация нового уникального пользователя успешна')
    def test_register_unique_user_successful(self):
        user = create_user_data()
        payload = user_attr_to_dict_converter(user)

        response = requests.post(Endpoints.REGISTER_ENDPOINT, data=payload)
        assert response.status_code == 200 and '"success":true' in response.text

    @allure.title('Повторная регистрация уже зарегистрированного пользователя неуспешна')
    def test_register_user_already_registered_unsuccessful(self, registered_user):
        payload = user_attr_to_dict_converter(registered_user)

        response = requests.post(Endpoints.REGISTER_ENDPOINT, data=payload)
        assert response.status_code == 403 and response.text == ResponseTexts.REGISTER_USER_ALREADY_REGISTERED

    @allure.title('Пользователь не может зарегистрироваться без обязательных полей')
    @pytest.mark.parametrize('not_full_user_data',
                             [
                                 'user_without_email',
                                 'user_without_password',
                                 'user_without_name'
                             ], ids=['регистрация без email',
                                     'регистрация без пароля',
                                     'регистрация без имени']
                             )
    def test_register_user_without_required_field(self, request, not_full_user_data):
        payload = request.getfixturevalue(not_full_user_data)
        response = requests.post(Endpoints.REGISTER_ENDPOINT, data=payload)
        assert response.status_code == 403 and response.text == ResponseTexts.REGISTER_USER_WITHOUT_REQUIRED_FIELD
