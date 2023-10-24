import sqlite3
conn = sqlite3.connect('acer.db')
print("opened database succefully")
conn.execute("INSERT INTO EMPLOYE(ID, NAME, AGE, ADDRESS, SALARY)\
 VALUES(1, 'Jeff', 32,'Califonia',45000.00 )")

conn.execute("INSERT INTO EMPLOYE(ID, NAME, AGE, ADDRESS, SALARY)\
 VALUES(2, 'Ali', 22,'NewYork',75000.00 )")

conn.execute("INSERT INTO EMPLOYE(ID, NAME, AGE, ADDRESS, SALARY)\
 VALUES(3, 'Joyce', 30,'Boston',400000.00 )")

conn.execute("INSERT INTO EMPLOYE(ID, NAME, AGE, ADDRESS, SALARY)\
 VALUES(4, 'Irene', 42,'Aston',50000.00 )")

conn.commit()
print("Records updated successfully")
conn.close()