import requests
import os

class ChirpstackLogin:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.url = f"{os.getenv('URL')}/api/internal/login"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def login(self):
        data = {"email": self.email, "password": self.password}
        response = requests.post(self.url, headers=self.headers, json=data)

        if response.status_code == 200:
            return response.json().get("jwt")  # Extract and return the JWT token
        else:
            print("Login failed:", response.status_code, response.text)
            return None
