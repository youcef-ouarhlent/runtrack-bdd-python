import mysql.connector

mydb = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = 'Zakaria13',
    database = 'entreprise',
)

mycursor = mydb.cursor(buffered=True)
mycursor.execute('SELECT * FROM employe INNER JOIN service ON employe.id_service = service.id')
cursor = mycursor.fetchall()

class Salarie:
    def __init__(self, id, nom, prenom, salaire, id_service):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire
        self.id_service = id_service

    def create(self):
        mycursor.execute(f"INSERT INTO employe VALUES ({self.id}, '{self.nom}', '{self.prenom}', {self.salaire}, {self.id_service})")
        mydb.commit()

    def read(self):
        mycursor.execute(f"SELECT * FROM employe WHERE id = {self.id}")
        return mycursor.fetchone()
    
    def update(self):
        mycursor.execute(f"UPDATE employe SET nom = '{self.nom}', prenom = '{self.prenom}', salaire = {self.salaire}, id_service = {self.id_service} WHERE id = {self.id}")
        mydb.commit()

    def delete(self):
        mycursor.execute(f"DELETE FROM employe WHERE id = {self.id}")
        mydb.commit()

creer = Salarie(18, 'Renoul', 'Jean', 2502.15, 2)
creer.create()

lire = Salarie(18, "", "", "", "")
print(lire.read())

modifier = Salarie(18, 'Rasoanaivo', 'Jean', 4500.65, 3)
modifier.update()
        
supprimer = Salarie(18, "", "", "", "")
supprimer.delete()


print(cursor)

mycursor.close()
mydb.close()