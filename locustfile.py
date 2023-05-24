from locust import HttpUser, task, between
import random

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    @task
    def load_index(self):
        self.client.get("/")
    
    @task
    def load_data(self):
        self.client.get("/data")

    @task
    def post_index(self):
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        self.client.post("/", data={'S': random.uniform(100, 1000),
            'K': random.uniform(100, 1500),
            'T': random.uniform(30, 360)/360,
            'r': random.uniform(0.01, 0.1),
            'q': random.uniform(0.01, 0.1),
            'sigma': random.uniform(0.01, 0.1),}, headers=headers)
