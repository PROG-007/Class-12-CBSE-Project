import pymysql
from classes import project_secrets

conn = pymysql.connect(
    host='localhost',
    user=project_secrets.databaseSecrets["user"],
    password=project_secrets.databaseSecrets["password"],
    database=project_secrets.databaseSecrets["database"]
)

cursor = conn.cursor()

cursor.execute("use class12")
cursor.execute("DELETE FROM credentials;")
cursor.execute("DELETE FROM creditcard;")
cursor.execute("DELETE FROM accounts;")

cursor.close()
conn.close()