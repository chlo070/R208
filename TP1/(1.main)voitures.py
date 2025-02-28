car = Voitures("Renault", "Clio", 2018) # Création d’une instance.
caisse = car.modele # Lecture d’un attribut d’instance.
print(f"J’ai une {car.marque} {caisse} de {car.annee} !") # Affichage.
car.annee = 2020 # Ecriture (modification) d’un attribut d’instance.
print(f"J’ai une {car.marque} {caisse} de {car.annee} !")