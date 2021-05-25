import requests


def get_currency_names(currencies):
    names = []
    for d in currencies:
        names.append(d['name'])

    return ",".join(names)


code = input("Enter country code :")
resp = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")
if resp.status_code == 404:
    print("Sorry! Country not found!")
    exit()

country = resp.json()

print(f"Name        : {country['name']}")
print(f"Capital     : {country['capital']}")
print(f"Region      : {country['region']}")
print(f"Population  : {country['population']}")
print(f"Currencies  : {get_currency_names(country['currencies'])}")
print(f"Borders     : {','.join(country['borders'])}")
