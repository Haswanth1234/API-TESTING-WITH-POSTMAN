import unittest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

class TestUserAPI(unittest.TestCase):

    def test_get_all_users(self):
        response = requests.get(BASE_URL, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

    def test_get_single_user(self):
        response = requests.get(f"{BASE_URL}/1", headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], 1)

    def test_create_user(self):
        payload = {
            "name": "John Doe",
            "email": "john@example.com",
            "username": "johndoe"
        }
        response = requests.post(BASE_URL, json=payload, headers=headers)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['name'], "John Doe")

    def test_update_user(self):
        payload = {
            "name": "Updated Name",
            "email": "updated@example.com",
            "username": "updateduser"
        }
        response = requests.put(f"{BASE_URL}/1", json=payload, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], "Updated Name")

    def test_delete_user(self):
        response = requests.delete(f"{BASE_URL}/1", headers=headers)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
