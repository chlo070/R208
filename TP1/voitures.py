#classe
class Voitures():
    # Constructeur avec 3 arguments...
    def __init__(self, marque="Ferrari", modele="SF90_spider", annee=2010) :
        # Trois attributs d’instance...
        self.marque = marque
        self.annee = annee
        self.modele = modele

    def __str__(self):
        # Redéfinition pour le print(instance)...
        return f"Valeurs des attributs de l’instance : {self.marque} {self.modele} {self.annee}"

""" NB :
# Avant la redéfinition…
<__main__.Voitures object at 0x102811fd0>  #la référence
# Après la redéfinition…
Valeurs des attributs de l’instance : Renault Clio 2020
"""

#main
car = Voitures("Renault", "Clio", 2018) # Création d’une instance.
caisse = car.modele # Lecture d’un attribut d’instance.
print(f"J’ai une {car.marque} {caisse} de {car.annee} !") # Affichage.
car.annee = 2020 # Ecriture (modification) d’un attribut d’instance.
print(f"J’ai une {car.marque} {caisse} de {car.annee} !")
print(car)
# Création d'une 2e instance
car2 = Voitures("Peugeot", "308", 2016)
print(car2)
# Création d’une 3e instance.
car3 = Voitures("Bugatti", "Veyron")
print(car3)
# Création d’une 4e instance.
car4 = Voitures()
print(car4)
# Création d’une 5e instance.
car5 = Voitures("F40")
print(car5)
# Création d’une 6e instance.
car6 = Voitures(modele = "296_GTS")
print(car6)
#12. Affichez « type(voiture6) » ou son équivalent : « voiture6._ _class_ _ ».
print(type(car6))
#13. Affichez « vars(voiture6) » ou son équivalent : « voiture6._ _dict_ _ ».
print(vars(car6))
#14. Affichez « dir(voiture6) »…
print(dir(car6))

