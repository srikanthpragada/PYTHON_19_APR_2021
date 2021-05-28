# Display count of employees and average salary

import sqlite3

try:
    con = sqlite3.connect(r"c:\classroom\apr19\hr.db")
    cur = con.cursor()
    cur.execute("select count(*), avg(salary) from employees")  # SQL Command
    count, avg = cur.fetchone()
    print(f"Count   : {count:10}")
    print(f"Average : {avg:10.0f}")
    cur.close()
    con.close()
except Exception as ex:
    print('Error :', ex)
