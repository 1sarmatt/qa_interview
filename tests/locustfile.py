from locust import HttpUser, task, between

class TaskTrackerUser(HttpUser):
    wait_time = between(1, 3)  # задержка между запросами

    def on_start(self):
        # логин перед началом сессии
        response = self.client.post("/api/login", json={
            "email": "testuser@example.com",
            "password": "password123"
        })
        token = response.json().get("token")
        self.headers = {"Authorization": f"Bearer {token}"}

    @task(2)
    def create_task(self):
        self.client.post("/api/tasks", json={
            "title": "Load Test Task",
            "description": "Task for performance testing"
        }, headers=self.headers)

    @task(1)
    def get_tasks(self):
        self.client.get("/api/tasks", headers=self.headers)

    @task(1)
    def search_tasks(self):
        self.client.get("/api/tasks/search?query=Load", headers=self.headers)
