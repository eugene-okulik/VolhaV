import requests
import pytest
import allure

url = 'http://objapi.course.qa-practice.com/object'


@allure.feature('Objects')
@allure.story('Get object')
@allure.title('Get the list of objects')
@pytest.mark.medium
def test_get_all_objects(print_start_and_completed, print_before_and_after):
    response = requests.get(url).json()
    assert len(response) == 1, 'not all posts returned'


@allure.feature('Objects')
@allure.story('Get object')
@allure.title('Get one object by id')
def test_get_one_object(print_before_and_after, new_object):
    post_id = new_object
    response = requests.get(f'{url}/{post_id}')
    assert response.status_code == 200


@allure.feature('Objects')
@allure.story('Manipulate objects')
@allure.title('New object creating')
@pytest.mark.critical
@pytest.mark.parametrize('name', ['cat', 'dog', 'bird'])
def test_post_an_object(print_before_and_after, name):
    with allure.step('Prepare test data'):
        body = {
            "name": name,
            "data": {"Klichka": "Mishel", "age": 7}
        }
        headers = {"Content-Type": "application/json"}
    with allure.step('Run request to create a post'):
        response = requests.post(url, json=body, headers=headers)
        response_data = response.json()
    with allure.step('Check response code is 200'):
        assert response.status_code == 200, "Status code is incorrect"
    with allure.step('Check that "name" parameter is exist'):
        assert "name" in response_data, "There is no 'name' value in object"
    with allure.step('Check that "data" parameter is exist'):
        assert "data" in response_data, "There is no 'data' value in object"


@allure.feature('Objects')
@allure.story('Manipulate posts')
@allure.title('Fully updating an object')
def test_put_an_object(new_object, print_before_and_after):
    object_id = new_object
    body = {
        "name": "Bird",
        "data": {"Klichka": "Gosha"}
    }
    headers = {"Content-Type": "application/json"}

    responce = requests.put(f'{url}/{object_id}', json=body, headers=headers).json()
    assert responce['name'] == "Bird"


@allure.feature('Objects')
@allure.story('Manipulate posts')
@allure.title('Partly updating an object')
def test_patch_an_object(new_object, print_before_and_after):
    object_id = new_object
    body = {
        "data": {"Klichka": "Nusha"}
    }
    headers = {"Content-Type": "application/json"}

    response = requests.patch(f'{url}/{object_id}', json=body, headers=headers).json()
    assert response["data"]["Klichka"] == "Nusha"


@allure.feature('Objects')
@allure.story('Manipulate posts')
@allure.title('Deleting an object')
def test_delete_a_post(new_object, print_before_and_after):
    with allure.step(f'Run get request for post with id {new_object}'):
        response = requests.delete(f'{url}/{new_object}')
    with allure.step(f'Check that post id is {new_object}'):
        assert response.status_code == 200


@allure.feature('Example')
@allure.story('Equals')
@allure.title('Print the num function')
def test_num(num):
    print(num)
