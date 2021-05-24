import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()  # Array of JSON objects to list of dict

for c in countries:
    c['area'] = 0 if c['area'] is None else c['area']
    print(f"{c['name']:50}  {c['capital']:20}  {c['area']:10}  ")
