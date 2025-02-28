#main exo 2
from obj_voiture import Voitures

# Création d’une instance.
carA = Voitures("Renault", "Captur_TCE_90ch",2018, 20000, "Gris foncé", 7.2)
caisse = carA.modele  # Lecture d’un attribut d’instance.
print(carA)  # Affichage.
# Création d’une 2e instance.
carB = Voitures("Renault", "Clio_TCE_100ch",2018, 17000, "Bleu nuit", 5.5)
caisse = carB.modele  # Lecture d’un attribut d’instance.
print(carB)  # Affichage.
# Test de la méthode calcul_consommation
print("Consommation :", carA.calcul_consommation(int(input("Quelle est la distance parcourue?"))))
print("Consommation :", carB.calcul_consommation(int(input("Quelle est la distance parcourue?"))))
# Test de la méthode calcul_prix
print("Prix :", carA.calcul_prix(1000))
print("Prix :", carB.calcul_prix(1000))

