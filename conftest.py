import pytest
from helpers import create_user_data, delete_user, register_user, create_burger
from data import WrongBurgerData, ExpectedResults


@pytest.fixture()
def user_data():
    user = create_user_data()
    yield user
    delete_user(user)


@pytest.fixture()
def registered_user():
    registered_user = register_user()
    yield registered_user
    delete_user(registered_user)


@pytest.fixture()
def user_without_email():
    user_without_email = create_user_data()
    user_data = {
        'email': user_without_email.password,
        'password': user_without_email.name
    }
    return user_data


@pytest.fixture()
def user_without_password():
    user_without_password = create_user_data()
    user_data = {
        'email': user_without_password.email,
        'password': user_without_password.name
    }
    return user_data


@pytest.fixture()
def user_without_name():
    user_without_name = create_user_data()
    user_data = {
        'email': user_without_name.email,
        'password': user_without_name.password
    }
    return user_data


@pytest.fixture()
def get_user_password(registered_user):
    new_user_password = registered_user.password
    return new_user_password


@pytest.fixture()
def get_user_email(registered_user):
    new_user_email = registered_user.email
    return new_user_email


@pytest.fixture(params=['with_correct_ingredients', 'with_wrong_ingredients', 'without_ingredients'])
def ingredient_options(request):
    if request.param == 'with_correct_ingredients':
        burger = create_burger()
        expected_result = ExpectedResults.CREATE_ORDER_WITH_CORRECT_INGREDIENTS
        return burger, expected_result
    elif request.param == 'with_wrong_ingredients':
        wrong_burger = WrongBurgerData.WRONG_BURGER_INGREDIENTS
        expected_result = ExpectedResults.CREATE_ORDER_WITH_WRONG_INGREDIENTS
        return wrong_burger, expected_result
    elif request.param == 'without_ingredients':
        expected_result = ExpectedResults.CREATE_ORDER_WITHOUT_INGREDIENTS
        return [], expected_result
