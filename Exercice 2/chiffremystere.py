import random

def chiffre_mystere():
    nombre_mystere = random.randint(1, 100)
    nombre_essais = 0
    chiffre_trouve = False

    while not chiffre_trouve:
        proposition = int(input("devinez le nombre entre 1 et 100 : "))
        nombre_essais += 1

        if proposition < nombre_mystere:
            print("trop petit!")
        elif proposition > nombre_mystere:
            print("trop grand!")
        else:
            print("félicitations! vous avez trouvé le nombre en", nombre_essais, "essais.")
            chiffre_trouve = True

chiffre_mystere()
