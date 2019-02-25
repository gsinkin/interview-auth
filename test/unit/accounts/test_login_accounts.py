import json
from uuid import UUID
from test.unit import BaseTestCase
from test.fixtures import AccountFixtures


class LoginAccountsTests(BaseTestCase):

    FIXTURES = [AccountFixtures]

    def test_login_account(self):
        request_data = json.dumps(
            {
                "email": "gabriel.sinkin@gmail.com",
                "password": "Password1!",
            }
        )
        headers = {
            "Content-type": "application/json"
        }
        response = self.client.post(
            "/v3/accounts/login",
            headers=headers,
            data=request_data,
        )
        self.assertEqual(response.status_code, 200)
        response_data = response.json
        self.assertTrue(response_data["api_key"])

    def test_login_invalid_info(self):
        request_data = {
            "email": "gabriel.sinkin@gmail.com",
            "password": "Password1!",
        }
        headers = {
            "Content-type": "application/json"
        }
        derp_fields = ["email", "password"]
        for derp_field in derp_fields:
            derp_data = request_data.copy()
            derp_data[derp_field] = "derp"

            response = self.client.post(
                "/v3/accounts/login",
                headers=headers,
                data=json.dumps(derp_data),
            )
            self.assertEqual(response.status_code, 401)

    def test_login_missing_info(self):
        request_data = {
            "email": "gabriel.sinkin@gmail.com",
            "password": "Password1!"
        }
        headers = {
            "Content-type": "application/json"
        }

        def empty(req_data, key):
            req_data[key] = ""

        def none(req_data, key):
            req_data[key] = None

        def deleted(req_data, key):
            del req_data[key]

        test_lambdas = (empty, none, deleted)
        for key, value in request_data.items():
            derp_data = request_data.copy()
            for test_lambda in test_lambdas:
                test_lambda(derp_data, key)

                response = self.client.post(
                    "/v3/accounts/login",
                    headers=headers,
                    data=json.dumps(derp_data),
                )
                self.assertEqual(response.status_code, 401)
                self.assertEqual(
                    response.json,
                    {
                        "message": "email and password required"
                    }
                )
