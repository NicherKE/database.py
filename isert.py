import sqlite3

conn = sqlite3.connect('example.db')
print("Opened dellpythonclass4_database successfully")

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
                VALUES(1, 'EMOBILIS', 7, 'WESTLANDS', 10000.00)");

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
                VALUES(2, 'Safaricom', 10, 'DAGORETI', 205000.00)");

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
                VALUES(3, 'Microsoft', 20, 'WESTLANDS', 2000.00)");

conn.execute("INSERT INTO COMPANY1(ID, NAME, AGE, ADDRESS, SALARY)\
                VALUES(4, 'Facebook', 15, 'Nairobi, KENYA', 50000.00)");

conn.commit()
print("Records created successfully")
conn.close()
