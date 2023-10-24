import sqlite3
conn = sqlite3.connect("acer.db")
print("open data base succefully")
conn.execute('''CREATE TABLE EMPLOYE(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')
print("table printed successfully")
conn.close()