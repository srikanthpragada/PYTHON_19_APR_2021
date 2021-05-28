# List employees from EMPLOYEES table of hr.db

import sqlite3

try:
    con = sqlite3.connect(r"c:\classroom\apr19\hr.db")
    print("Connected Successfully!")
    con.close()
except Exception as ex:
    print('Error :', ex)

