#main exo 2
from obj_voiture import Voitures

carA = Voitures("Renault", "Captur_TCE_90ch",2018)  # Création d’une instance.
caisse = carA.modele  # Lecture d’un attribut d’instance.
print(f"J’ai une {carA.marque} {caisse} de {carA.annee} !")  # Affichage.
carB = Voitures("Renault", "Clio_TCE_100ch",2018)  # Création d’une instance.
caisse = carB.modele  # Lecture d’un attribut d’instance.
print(f"J’ai une {carB.marque} {caisse} de {carB.annee} !")  # Affichage.