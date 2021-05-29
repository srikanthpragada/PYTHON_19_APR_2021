# Load data from JSON file to DB

import sqlite3
import json

f = open("employees.json", "rt")
employees = json.load(f)    # Convert array of JSON objects to list of dict

con = sqlite3.connect(r"c:\classroom\apr19\hr.db")
cur = con.cursor()
count = 0
for emp in employees:
    cur.execute("insert into employees(fullname,job,salary) values(?,?,?)",
                (emp['name'], emp['job'], emp['salary']))
    count += 1

con.commit()
cur.close()
con.close()
print(f"Inserted {count} employees")
