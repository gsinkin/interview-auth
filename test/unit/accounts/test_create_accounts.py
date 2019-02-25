import json
from uuid import UUID
from test.unit import BaseTestCase


class CreateAccountsTests(BaseTestCase):

    def test_create_account(self):
        request_data = json.dumps(
            {
                "email": "gsinkin@earnup.com",
                "password": "Password1!",
            }
        )
        headers = {
            "Content-type": "application/json"
        }
        response = self.client.post(
            "/v3/accounts",
            headers=headers,
            data=request_data,
        )
        self.assertEqual(response.status_code, 200)
        response_data = response.json
        api_key = response_data["api_key"]
        self.assertTrue(UUID(api_key))

        # should not be able to create existing account
        response = self.client.post(
            "/v3/accounts",
            headers=headers,
            data=request_data,
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"message": "Account exists"})

    def test_create_account_missing_info(self):
        request_data = {
            "email": "gsinkin@earnup.com",
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
                    "/v3/accounts",
                    headers=headers,
                    data=json.dumps(derp_data),
                )
                self.assertEqual(response.status_code, 400)
                self.assertEqual(
                    response.json,
                    {
                        "message": "email and password required"
                    }
                )
