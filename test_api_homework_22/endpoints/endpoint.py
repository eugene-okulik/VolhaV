import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None
    headers = {"Content-Type": "application/json"}

    @allure.step('Check that name is the same as sent')
    def check_response_name_is_correct(self, name):
        self.json = self.response.json()
        assert self.json['name'] == name

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200

    @allure.step('Check that 400 error received')
    def check_negative_request(self):
        assert self.response.status_code == 400, "Status code is incorrect"
