import requests
import allure
from test_api_homework_22.endpoints.endpoint import Endpoint

class DeleteObject(Endpoint):
    @allure.step('Delete the object')
    def delete_an_object(self, object_id):
        self.response = requests.delete(f'{self.url}/{object_id}')
        return self.response