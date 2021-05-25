import requests

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()  # Array of JSON objects to list of dict

for c in sorted(countries, key=lambda d: d['population'], reverse=True)[:10]:
    print(f"{c['name']:50}  {c['population']:10}")
