names = ['Bill', 'Andy', 'Mike', "Jack"]
emails = ['bill@gmail.com', 'andy@yahoo.com', 'mike@gmail.com']

for idx, name in enumerate(names):
    if idx < len(emails):
        email = emails[idx]
    else:
        email = 'Unknown'

    print(f"{name:10} {email}")
