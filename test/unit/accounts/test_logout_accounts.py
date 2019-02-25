import json
from uuid import UUID
from test.unit import BaseTestCase
from test.fixtures import AccountFixtures


class LogoutAccountsTests(BaseTestCase):

    FIXTURES = [AccountFixtures]

    def test_logout_account(self):
        headers = {
            "Content-type": "application/json",
            "X-API-Key": "123-456-7890",
        }
        response = self.client.get(
            "/v3/accounts/logout",
            headers=headers,
        )
        self.assertEqual(response.status_code, 204)

    def test_logout_invalid_api_key(self):
        headers = {
            "Content-type": "application/json",
            "X-API-Key": "123-456",
        }

        response = self.client.get(
            "/v3/accounts/logout",
            headers=headers,
        )
        self.assertEqual(response.status_code, 400)
