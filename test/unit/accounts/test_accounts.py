import json
from uuid import UUID
from test.unit import BaseTestCase


class AccountsTests(BaseTestCase):

    def test_create_account(self):
        response = self.client.post(
            "/v3/accounts",
            headers={
                "Content-type": "application/json"
            },
            data=json.dumps(
                {
                    "email": "gsinkin@earnup.com",
                    "password": "Password1!",
                }
            ),
        )
        self.assertEquals(response.status_code, 200)
        response_data = response.json
        api_key = response_data["api_key"]
        self.assertTrue(UUID(api_key))
