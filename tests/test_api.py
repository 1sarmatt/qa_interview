import unittest
import requests
import logging

BASE_URL = "http://127.0.0.1:5000/api"  # Замените на актуальный URL

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("test_log.log"),
        logging.StreamHandler()
    ]
)

class TestTaskTrackerAPI(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()
        self.user = {"email": "testuser@example.com", "password": "password123"}
        response = self.session.post(f"{BASE_URL}/login", json=self.user)
        logging.info(f"Login response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)
        self.token = response.json().get("token")
        self.session.headers.update({"Authorization": f"Bearer {self.token}"})

    def test_create_task(self):
        task = {
            "title": "Test Task",
            "description": "Test Description",
            "status": "To Do"
        }
        response = self.session.post(f"{BASE_URL}/tasks", json=task)
        logging.info(f"Create task response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())

    def test_search_task(self):
        keyword = "Test"
        response = self.session.get(f"{BASE_URL}/tasks/search", params={"query": keyword})
        logging.info(f"Search task response: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_task_without_title(self):
        task = {
            "description": "No title",
            "status": "To Do"
        }
        response = self.session.post(f"{BASE_URL}/tasks", json=task)
        logging.warning(f"Invalid task creation: {response.status_code} - {response.text}")
        self.assertEqual(response.status_code, 400)

    def tearDown(self):
        self.session.close()

if __name__ == "__main__":
    unittest.main()