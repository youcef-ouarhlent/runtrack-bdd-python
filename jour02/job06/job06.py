import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Zakaria13",
    database="laplateforme"
)
cursor = mydb.cursor()
cursor.execute("SELECT SUM(capacite) FROM salle")
result = cursor.fetchone()[0] 
print("La capacite de toutes les salles est de:", result)
cursor.close()
mydb.close()
