## Дипломный проект. Задание 2: API-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

**Созданы API-тесты, покрывающие эндпоинты:**

Создание пользователя:

* создать уникального пользователя;
* создать пользователя, который уже зарегистрирован;
* создать пользователя и не заполнить одно из обязательных полей.

Логин пользователя:

* логин под существующим пользователем,
* логин с неверным логином и паролем.

Изменение данных пользователя:

* с авторизацией,
* без авторизации,

Создание заказа:

* с авторизацией,
* без авторизации,
* с ингредиентами,
* без ингредиентов,
* с неверным хешем ингредиентов.

Получение заказов конкретного пользователя:

* авторизованный пользователь,
* неавторизованный пользователь.

### Структура проекта

- `tests` - пакет, содержащий тесты, разделенные по эндпоинтам
- `conftest.py` - содержит фикстуры
- `data.py` - содержит url, тестовые данные
- `helpers.py` - содержит вспомогательные функции

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание allure-отчета**

>  `$ pytest tests --alluredir=allure_results`

**Просмотр allure-отчета**

>  `$ allure serve allure_results`
