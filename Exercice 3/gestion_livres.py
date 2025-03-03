import sqlite3

# Connexion à db
conn = sqlite3.connect('bibliotheque.db')
cursor = conn.cursor()

# Création de la table 
cursor.execute('''
CREATE TABLE IF NOT EXISTS livres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    annee_publication INTEGER NOT NULL,
    disponible BOOLEAN NOT NULL CHECK (disponible IN (0, 1))
)
''')

# Connexion
conn.commit()
conn.close()

def ajout_livre(titre, auteur, annee_publication, disponible):
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO livres (titre, auteur, annee_publication, disponible)
        VALUES (?, ?, ?, ?)
    ''', (titre, auteur, annee_publication, disponible))
    conn.commit()
    conn.close()
    print("votre livre est ajouté.")

def livres_dispos():
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres WHERE disponible = 1')
    livres = cursor.fetchall()
    conn.close()
    return livres

def recherche_partitre(titre):
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres WHERE titre LIKE ?', ('%' + titre + '%',))
    livres = cursor.fetchall()
    conn.close()
    return livres

def maj_disponibilite(id, disponible):
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE livres SET disponible = ? WHERE id = ?', (disponible, id))
    conn.commit()
    conn.close()
    print("la disponibilité du livre a été mise à jour.")

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1 - ajout d'un nouveau livre")
        print("2 - consultation de la liste des livres disponibles")
        print("3 -recherche d'un livre par titre")
        print("4 - mise à jour l'état de disponibilité d'un livre")
        print("5 - Quitter")
        
        choix = input("Choisissez une option : ")
        
        if choix == "1":
            titre = input("Entrez le titre du livre : ")
            auteur = input("Entrez l'auteur du livre : ")
            annee_publication = int(input("Entrez l'année de publication : "))
            disponible = int(input("Le livre est-il disponible ? (1 = Oui, 0 = Non) : "))
            ajout_livre(titre, auteur, annee_publication, disponible)
        
        elif choix == "2":
            livres_disponibles = livres_dispos()
            print("Livres disponibles :")
            for livre in livres_disponibles:
                print(livre)
        
        elif choix == "3":
            titre_recherche = input("Entrez le titre du livre à rechercher : ")
            livres_trouves = recherche_partitre(titre_recherche)
            print(f"Livres trouvés pour le titre '{titre_recherche}' :")
            for livre in livres_trouves:
                print(livre)
        
        elif choix == "4":
            id_livre = int(input("mettez l'id du livre : "))
            disponible = int(input("ce livre est-il disponible ? (1 = Oui, 0 = Non) : "))
            maj_disponibilite(id_livre, disponible)
        
        elif choix == "5":
            break
        
        else:
            print("Erreur. Reessayez!")