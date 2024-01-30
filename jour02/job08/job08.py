import mysql.connector

mydb = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    password = 'Zakaria13',
    database = 'zoo',
)

mycursor = mydb.cursor(buffered=True)
mycursor.execute('SELECT * FROM animal')
mycursor.execute('SELECT * FROM cage')
cursor = mycursor.fetchall()

class Directeur:
    def __init__(self, nom, race, id_type_de_cage, date_de_naissance, pays_origine):
        self.nom = nom
        self.race = race
        self.id_type_de_cage = id_type_de_cage
        self.date_de_naissance = date_de_naissance
        self.pays_origine = pays_origine

    def ajouter_animal(self):
        mycursor.execute(f"INSERT INTO animal (nom, race, id_type_de_cage, date_de_naissance, pays_origine) VALUES ('{self.nom}', '{self.race}', '{self.id_type_de_cage}', '{self.date_de_naissance}', '{self.pays_origine}')")
        mydb.commit()

    def supprimer_animal(self):
        mycursor.execute(f"DELETE FROM animal WHERE nom = '{self.nom}'")
        mydb.commit()

    def modifier_animal(self, nom_animal_a_modifier, nouvelle_valeur):
        mycursor.execute(f"UPDATE animal SET nom = '{nouvelle_valeur}' WHERE nom = '{nom_animal_a_modifier}'")
        mydb.commit()

    def modifier_cage(self, id_cage_a_modifier, nouvelle_superficie, nouvelle_capacite):
        mycursor.execute(f"UPDATE cage SET superficie = '{nouvelle_superficie}', capacite_max = '{nouvelle_capacite}' WHERE id = '{id_cage_a_modifier}'")
        mydb.commit()

    def afficher_animaux(self):
        mycursor.execute("SELECT * FROM animal INNER JOIN cage ON animal.id_type_de_cage = cage.id")
        mydb.commit()
        print(mycursor.fetchall())

    def calculer_superficie_totale(self):
        mycursor.execute("SELECT SUM(superficie) FROM cage")
        mydb.commit()
        result = mycursor.fetchone()[0]
        superficie_totale = int(result)
        print(f"La superficie totale est de {superficie_totale} m2")

while True:
    action = input("Souhaitez-vous ajouter (A) ou modifier (M) ou supprimer (S) un animal ? ou modifier (MC) une cage ? ou afficher les animaux (AF)? ou calculer la superficie (CS)?(Q pour quitter) : ").upper()

    if action == 'Ajouter' or action == 'A' or action == 'ajouter' or action == 'a':
        nom = input("Nom de l'animal : ")
        race = input("Race de l'animal : ")
        id_type_de_cage = input("ID du type de cage : ")
        date_de_naissance = input("Date de naissance de l'animal (format YYYY-MM-DD) : ")
        pays_origine = input("Pays d'origine de l'animal : ")

        animal = Directeur(nom, race, id_type_de_cage, date_de_naissance, pays_origine)
        animal.ajouter_animal()

    elif action == 'Modifier' or action == 'M' or action == 'modifier' or action == 'm':
        modifier = input("Nom de l'animal à modifier : ")
        nouvelle_valeur = input("Nouvelle valeur : ")
        animal_a_modifier = Directeur("", "", "", "", "")
        animal_a_modifier.modifier_animal(modifier, nouvelle_valeur) 

    elif action == 'Supprimer' or action == 'S' or action == 'supprimer' or action == 's':
        supprimer = input("Nom de l'animal à supprimer : ")
        animal_a_supprimer = Directeur(supprimer, "", "", "", "")
        animal_a_supprimer.supprimer_animal()

    elif action == 'Modifier cage' or action == 'MC' or action == 'modifier cage' or action == 'mc':
        id_cage_a_modifier = input("ID de la cage à modifier : ")
        nouvelle_superficie = input("Nouvelle superficie : ")
        nouvelle_capacite = input("Nouvelle capacité : ")
        cage_a_modifier = Directeur("", "", "", "", "")
        cage_a_modifier.modifier_cage(id_cage_a_modifier, nouvelle_superficie, nouvelle_capacite)

    elif action == 'Afficher' or action == 'AF' or action == 'afficher' or action == 'af':
        afficher = Directeur("", "", "", "", "")
        afficher.afficher_animaux()

    elif action == 'Calculer superficie' or action == 'CS' or action == 'calculer superficie' or action == 'cs':
        calculer = Directeur("", "", "", "", "")
        calculer.calculer_superficie_totale()

    elif action == 'Quit' or action == 'Q' or action == 'quit' or action == 'q':
        print("Merci d'avoir utilisé le programme!")
        break  

    else:
        print("Commande invalide.")


mycursor.close()
mydb.close()