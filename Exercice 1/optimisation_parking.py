longueur_parking = 120 
largeur_parking = 50    
longueur_place = 5 
largeur_place = 2.5     
distance_rangee = 1
tarif_journalier = 3000

places_par_rangee = largeur_parking // largeur_place
nombre_rangees = longueur_parking // (longueur_place + distance_rangee)
nombre_max_voitures = int(places_par_rangee * nombre_rangees)
revenu_max = nombre_max_voitures * tarif_journalier
espace_total = longueur_parking * largeur_parking
espace_bus = 0.15 * espace_total
espace_restant = espace_total - espace_bus
nombre_places_dispos_restants = (espace_restant // (longueur_place * largeur_place))
revenu_max_restant = int(nombre_places_dispos_restants * tarif_journalier)

print(f"Le nombre maximum de voitures pouvant être garées : {nombre_max_voitures}")
print(f"Le revenu maximum du parking sur une journée : {revenu_max} MGA")
print(f"Le nombre de places disponibles avec une zone réservée aux bus : {nombre_places_dispos_restants}")
print(f"Le revenu maximum du parking sur une journée avec la zone réservée aux bus : {revenu_max_restant} MGA")