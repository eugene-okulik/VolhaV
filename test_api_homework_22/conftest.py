import pytest
from test_api_homework_22.endpoints.create_object import CreateObject
from test_api_homework_22.endpoints.update_object import UpdateObject
from test_api_homework_22.endpoints.get_object import GetObject
from test_api_homework_22.endpoints.update_object_partly import UpdateObjectPartly
from test_api_homework_22.endpoints.delete_object import DeleteObject

test_payload = {
    "name": "Dog",
    "data": {"Klichka": "Bobik", "age": 3, "Type": "Haski"}
}


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def patch_changes_in_object():
    return UpdateObjectPartly()


@pytest.fixture()
def delete_object():
    return DeleteObject()


@pytest.fixture()
def new_test_object():
    create_test_object = CreateObject()
    responce = create_test_object.create_new_object(payload=test_payload)
    object_id = responce.json()["id"]
    yield object_id
    delete_test_object = DeleteObject()
    delete_test_object.delete_an_object(object_id)


@pytest.fixture()
def new_test_object_for_delete_method():
    create_test_object = CreateObject()
    responce = create_test_object.create_new_object(payload=test_payload)
    object_id = responce.json()["id"]
    yield object_id


@pytest.fixture()
def clean_object_after_test():
    created_objects_ids = []
    yield created_objects_ids
    if created_objects_ids:
        delete_test_object = DeleteObject()
        object_id = created_objects_ids[0]
        delete_test_object.delete_an_object(object_id)
