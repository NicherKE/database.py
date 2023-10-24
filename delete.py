import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("DELETE from COMPANY1 where id=2")
conn.commit()


cursor = conn.execute("SELECT id, name, address, age, salary from COMPANY1")

for row in cursor:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("ADDRESS =", row[2])
    print("AGE =", row[3])
    print("SALARY =", row[4])

print("Operation done successfully")
conn.close()