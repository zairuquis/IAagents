import requests

response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
joke = response.json().get("joke")

print(f"Broma: {joke}")
