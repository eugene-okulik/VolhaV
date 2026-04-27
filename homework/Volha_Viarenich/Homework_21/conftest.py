import pytest
import requests

base_url = 'http://objapi.course.qa-practice.com/object'

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

    responce = requests.post(base_url, json=body, headers=headers)
    object_id = responce.json()["id"]
    yield object_id
    requests.delete(f'{base_url}/{object_id}')


@pytest.fixture()
def num():
    return 1