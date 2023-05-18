import pymysql
import project_secrets

conn = pymysql.connect(
    host="localhost",
    user="root",
    password=project_secrets.secrectsDict["passworddb"],
    database="class12"
)

cursor = conn.cursor()

cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()

for table in tables:
    print(table[0])

cursor.close()
conn.close()
