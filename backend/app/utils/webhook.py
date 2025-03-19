import requests

def send_webhook(url: str, data: dict):
    response = requests.post(url, json=data)
    response.raise_for_status()
    return response.json()
