from locust import task, HttpUser
from test_api_homework_22.endpoints.create_object import CreateObject
from test_api_homework_22.endpoints.delete_object import DeleteObject
from test_api_homework_22.conftest import test_payload


class MainUser(HttpUser):
    headers = {"Content-Type": "application/json"}
    object_id = None

    def on_start(self):
        create_test_object = CreateObject()
        response = create_test_object.create_new_object(payload=test_payload)
        self.object_id = response.json()["id"]

    @task(1)
    def get_all_objects(self):
        self.client.get('/object', headers=self.headers)

    @task(3)
    def get_one_object(self):
        self.client.get(f'/object/{self.object_id}', headers=self.headers)

    def on_stop(self):
        if self.object_id:
            delete_test_object = DeleteObject()
            delete_test_object.delete_an_object(self.object_id)
