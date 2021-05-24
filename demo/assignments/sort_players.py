from datetime import datetime

f = open("Players.txt", "rt")
players = []
today = datetime.now()

for line in f:
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue
    try:
        dob = datetime.strptime(parts[1], '%d-%m-%Y')
        years = (today - dob).days // 365
        players.append((parts[0], years))
    except:
        pass

for name, age in sorted(players, key=lambda t: t[1]):
    print(f"{name:15} {age:2}")
