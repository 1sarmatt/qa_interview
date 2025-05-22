from locust import HttpUser, task, between

class TaskTrackerLoadTest(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_tasks(self):
        self.client.get("/api/tasks")

    @task
    def create_task(self):
        self.client.post("/api/tasks", json={
            "title": "Load Test",
            "description": "Performance testing",
            "status": "To Do"
        })