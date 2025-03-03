distance_livraion = 450 
consommation_camion = 14 
prix_carburant = 4800

litres_necessaires = (distance_livraion / 100) * consommation_camion
cout_total = litres_necessaires * prix_carburant

print("Litres de carburant nécessaires pour le trajet :", litres_necessaires)
print("Coût total du carburant :", cout_total, "Ariary")

nouvelle_consommation = consommation_camion * 0.8
nouvelle_litres_necessaires = (distance_livraion / 100) * nouvelle_consommation
nouveau_cout_total = nouvelle_litres_necessaires * prix_carburant

print("Nouveau modèle de camion :")
print("Litres de carburant nécessaires pour le trajet :", nouvelle_litres_necessaires)
print("Coût total du carburant :", nouveau_cout_total, "Ariary")
