import sqlite3
conn = sqlite3.connect("ku.db")
cursor = conn.cursor()
results = cursor.execute("SELECT * from biaoge")
for record in results:
    print("id = ",record[0])
    print("name = ",record[1])
    print("gender = ",record[2])
cursor.close()
conn.close()
