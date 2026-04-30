import pytest
import allure

TEST_DATA = [{"name": 'cat', "data": {"Klichka": "Mishel", "age": 7}},
             {"name": 'dog', "data": {"Klichka": "Bobik", "age": 1}},
             {"name": 'bird', "data": {"Klichka": "Gosha", "age": 2}}
             ]

NEGATIVE_DATA = [{"name": ["My name"], "body": "my body", "userId": 1},
                 {"name": {"My name2": ''}, "body": "my body2", "userId": 2}
                 ]


@allure.feature('Objects')
@allure.story('Get object')
@allure.title('Get the list of objects')
@pytest.mark.regression
def test_get_all_objects(get_object_endpoint):
    get_object_endpoint.get_all_objects()
    get_object_endpoint.check_that_status_is_200()


@allure.feature('Objects')
@allure.story('Get object')
@allure.title('Get one object by id')
@pytest.mark.smoke
def test_get_object_by_id(get_object_endpoint, new_test_object):
    get_object_endpoint.get_one_object_by_id(new_test_object)
    get_object_endpoint.check_that_status_is_200()


@allure.feature('Objects')
@allure.story('Manipulate objects')
@allure.title('New object creating')
@pytest.mark.smoke
@pytest.mark.parametrize('data', TEST_DATA)
def test_post_an_object(data, create_object_endpoint, clean_object_after_test):
    create_object_endpoint.create_new_object(payload=data)
    object_id = create_object_endpoint.response.json()["id"]
    clean_object_after_test.append(object_id)
    create_object_endpoint.check_that_status_is_200()
    create_object_endpoint.check_response_name_is_correct(data['name'])


@allure.feature('Objects')
@allure.story('Manipulate objects')
@allure.title('Negative case for object creating')
@pytest.mark.regression
@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_post_with_negative_data(create_object_endpoint, data):
    create_object_endpoint.create_new_object(payload=data)
    create_object_endpoint.check_negative_request()


@allure.feature('Objects')
@allure.story('Manipulate objects')
@allure.title('Fully updating an object')
@pytest.mark.smoke
def test_put_an_object(update_object_endpoint, new_test_object):
    payload = {
        "name": "Bird",
        "data": {"Klichka": "Gosha"}
    }
    update_object_endpoint.make_changes_in_object(new_test_object, payload)
    update_object_endpoint.check_that_status_is_200()
    update_object_endpoint.check_response_name_is_correct(payload['name'])


@allure.feature('Objects')
@allure.story('Manipulate objects')
@allure.title('Partly updating an object')
@pytest.mark.regression
def test_patch_an_object(patch_changes_in_object, new_test_object):
    payload = {
        "name": "Fish"
    }
    patch_changes_in_object.partly_changes_in_object(new_test_object, payload)
    patch_changes_in_object.check_that_status_is_200()
    patch_changes_in_object.check_response_name_is_correct(payload['name'])


@allure.feature('Objects')
@allure.story('Manipulate objects')
@allure.title('Deleting an object')
def test_delete_an_object(delete_object, new_test_object_for_delete_method):
    delete_object.delete_an_object(new_test_object_for_delete_method)
    delete_object.check_that_status_is_200()
