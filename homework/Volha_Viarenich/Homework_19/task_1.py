import requests

url = 'http://objapi.course.qa-practice.com/'


def get_all_objects():
    response = requests.get(url).json()
    assert len(response) == 100, 'not all posts returned'


def get_one_object():
    post_id = 13
    response = requests.get(f'{url}{post_id}').json()
    assert response['id'] == post_id


def post_an_object():
    body = {
        "name": "Cat",
        "data": {"Klichka": "Mishel", "age": 7}
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=body, headers=headers)
    response_data = response.json()

    assert response.status_code == 201, 'Status code is incorrect'
    assert response_data["name"] == "Cat", 'name is incorrect'
    assert response_data["data"]["Klichka"] == "Mishel", "Klichka is incorrect"
    assert response_data["data"]["age"] == 7, "Age is incorrect"
    assert "name" in response_data, "There is no 'name' value in object"
    assert "data" in response_data, "There is no 'data' value in object"


def new_object():
    body = {
        "name": "Dog",
        "data": {"Klichka": "Bobik", "age": 3, "Type": "Haski"}
    }
    headers = {"Content-Type": "application/json"}

    responce = requests.post(url, json=body, headers=headers)
    return responce.json()["id"]


def clear(object_id):
    requests.delete(f'{url}{object_id}')


def put_an_object():
    object_id = new_object()
    body = {
        "name": "Bird",
        "data": {"Klichka": "Gosha"}
    }
    headers = {"Content-Type": "application/json"}

    responce = requests.put(f'{url}{object_id}', json=body, headers=headers).json()
    assert responce['name'] == "Bird"
    clear(object_id)


def patch_an_object():
    object_id = new_object()
    body = {
        "data": {"Klichka": "Nusha"}
    }
    headers = {"Content-Type": "application/json"}

    response = requests.put(f'{url}{object_id}', json=body, headers=headers).json()
    assert response["data"]["Klichka"] == "Nusha"
    clear(object_id)


def delete_a_post():
    object_id = new_object()
    response = requests.delete(f'{url}{object_id}')
    assert response.status_code == 204
