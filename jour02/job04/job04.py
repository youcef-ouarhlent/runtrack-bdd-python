import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Zakaria13",
    database="laplateforme"
)
cursor = mydb.cursor()
cursor.execute("SELECT nom,capacite FROM `salle`")
result = cursor.fetchall()
print(result)
cursor.close()
mydb.close()

