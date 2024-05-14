from databricks import sql
import os

connection = sql.connect(
    server_hostname="adb-2827753626774649.9.azuredatabricks.net",
    http_path="/sql/1.0/warehouses/61a4d720eac18b7f",
    access_token="<access-token>")

cursor = connection.cursor()

cursor.execute("SELECT * from range(10)")
print(cursor.fetchall())

cursor.close()
connection.close()
