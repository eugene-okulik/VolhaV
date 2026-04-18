import requests
import pytest

# Тест на создание объекта оформите так, чтобы он тестировал создание трёх разных объектов с помощью parametrize.
# Сделайте так, чтобы перед запуском всех тестов распечатывалось "Start testing", а по завершении всех тестов -
# "Testing completed"
# Сделайте так, чтобы перед каждым тестом распечатывалось "before test", а после каждого теста - "after test"
# Пометьте 1 тест как "critical", а один тест как "medium". Сделайте так, чтобы при выполнении тестов в терминале
# не было ошибок и ворнингов.
# Тесты на изменение, получение по id и удаление объекта сделайте независимыми.
# Т.е. сделайте так, чтобы перед запуском каждого из этих тестов запускалось выполнение предусловия -
# создание объекта для этого теста, в после теста, пусть созданный объект удаляется.


url = 'http://objapi.course.qa-practice.com/object'


@pytest.fixture(scope='session')
def print_start_and_completed():
    print("Start testing")
    yield
    print(" Testing completed")


@pytest.fixture()
def print_before_and_after():
    print("Before test")
    yield
    print(" After test")


@pytest.fixture()
def new_object():
    body = {
        "name": "Dog",
        "data": {"Klichka": "Bobik", "age": 3, "Type": "Haski"}
    }
    headers = {"Content-Type": "application/json"}

    responce = requests.post(url, json=body, headers=headers)
    object_id = responce.json()["id"]
    yield object_id
    requests.delete(f'{url}/{object_id}')


@pytest.mark.medium
def test_get_all_objects(print_start_and_completed, print_before_and_after):
    response = requests.get(url).json()
    assert len(response) == 1, 'not all posts returned'


def test_get_one_object(print_before_and_after, new_object):
    post_id = new_object
    response = requests.get(f'{url}/{post_id}')
    assert response.status_code == 200


@pytest.mark.critical
@pytest.mark.parametrize('name', ['cat', 'dog', 'bird'])
def test_post_an_object(print_before_and_after, name):
    body = {
        "name": name,
        "data": {"Klichka": "Mishel", "age": 7}
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=body, headers=headers)
    response_data = response.json()

    assert response.status_code == 200, "Status code is incorrect"
    assert "name" in response_data, "There is no 'name' value in object"
    assert "data" in response_data, "There is no 'data' value in object"


def test_put_an_object(new_object, print_before_and_after):
    object_id = new_object
    body = {
        "name": "Bird",
        "data": {"Klichka": "Gosha"}
    }
    headers = {"Content-Type": "application/json"}

    responce = requests.put(f'{url}/{object_id}', json=body, headers=headers).json()
    assert responce['name'] == "Bird"


def test_patch_an_object(new_object, print_before_and_after):
    object_id = new_object
    body = {
        "data": {"Klichka": "Nusha"}
    }
    headers = {"Content-Type": "application/json"}

    response = requests.patch(f'{url}/{object_id}', json=body, headers=headers).json()
    assert response["data"]["Klichka"] == "Nusha"


def test_delete_a_post(new_object, print_before_and_after):
    object_id = new_object
    response = requests.delete(f'{url}/{object_id}')
    assert response.status_code == 200
