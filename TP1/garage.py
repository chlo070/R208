#main exo 2
from obj_voiture import Voitures

carA = Voitures("Renault", "Captur_TCE_90ch",2018, 20000, "Gris foncé", 7.2)  # Création d’une instance.
caisse = carA.modele  # Lecture d’un attribut d’instance.
print(carA)  # Affichage.
carB = Voitures("Renault", "Clio_TCE_100ch",2018, 17000, "Bleu nuit", 5.5)  # Création d’une instance.
caisse = carB.modele  # Lecture d’un attribut d’instance.
print(carB)  # Affichage.