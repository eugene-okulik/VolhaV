import requests
import allure
from test_api_homework_22.endpoints.endpoint import Endpoint


class GetObject(Endpoint):
    @allure.step('Get the list of objects')
    def get_all_objects(self):
        self.response = requests.get(self.url)
        return self.response

    @allure.step('Get the one object by id')
    def get_one_object_by_id(self, object_id):
        self.response = requests.get(f'{self.url}/{object_id}')
        return self.response
