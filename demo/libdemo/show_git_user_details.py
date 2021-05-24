import requests

user = "srikanthpragada"
resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code == 404:
    print("Sorry! User not found!")

details = resp.json()

for key, value in details.items():
    print(f"{key:20}  {value}")
