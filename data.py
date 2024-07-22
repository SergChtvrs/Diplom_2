class Endpoints:
    MAIN_LINK = 'https://stellarburgers.nomoreparties.site'
    REGISTER_ENDPOINT = MAIN_LINK + '/api/auth/register'
    USER_ENDPOINT = MAIN_LINK + '/api/auth/user'
    USER_LOGIN_ENDPOINT = MAIN_LINK + '/api/auth/login'
    ORDER_ENDPOINT = MAIN_LINK + '/api/orders'
    INGREDIENTS_ENDPOINT = MAIN_LINK + '/api/ingredients'


class User:
    def __init__(self, email, password):
        self.name = "Марк Аврелий"
        self.email = email
        self.password = password
        self.access_token = None


class WrongUserData:
    WRONG_EMAIL = 'test@test.com'
    WRONG_PASSWORD = 'password'


class WrongBurgerData:
    WRONG_BURGER_INGREDIENTS = [6666666666666666, 77777777777777777]


class ExpectedResults:
    CREATE_ORDER_WITH_CORRECT_INGREDIENTS = 200
    CREATE_ORDER_WITH_WRONG_INGREDIENTS = 500
    CREATE_ORDER_WITHOUT_INGREDIENTS = 400


class ResponseTexts:
    REGISTER_USER_ALREADY_REGISTERED = '{"success":false,"message":"User already exists"}'
    REGISTER_USER_WITHOUT_REQUIRED_FIELD = '{"success":false,"message":"Email, password and name are required fields"}'
    USER_LOGIN_WITH_WRONG_PARAMS = '{"success":false,"message":"email or password are incorrect"}'
    GET_UNAUTHORIZED_USER_ORDERS = '{"success":false,"message":"You should be authorised"}'
    CREATE_ORDER_WITHOUT_INGREDIENTS = '{"success":false,"message":"Ingredient ids must be provided"}'
    UPDATE_USER_DATA_WITHOUT_AUTHORIZATION = '{"success":false,"message":"You should be authorised"}'
