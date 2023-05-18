import pymysql
import project_secrets

conn = pymysql.connect(
    host="localhost",
    user="root",
    password=project_secrets.secrectsDict["passworddb"],
    database="class12"
)

cursor = conn.cursor()

cursor.execute("DELETE FROM credentials;")
cursor.execute("DELETE FROM creditcard;")
cursor.execute("DELETE FROM accounts;")

cursor.close()
conn.close()