# List employees from EMPLOYEES table of hr.db

import sqlite3

try:
    con = sqlite3.connect(r"c:\classroom\apr19\hr.db")
    cur = con.cursor()
    cur.execute("select * from employees order by salary desc")  # SQL Command

    for id, name, job, salary in cur.fetchall():
        print(f"{id:2} {name:20} {job:10} {salary:10}")

    cur.close()
    con.close()
except Exception as ex:
    print('Error :', ex)
