#module exo 2
#class
class Voitures():
    prix_litre = 1.70
    # Constructeur avec 3 arguments...
    def __init__(self, marque="Ferrari", modele="SF90_spider", annee=2010, prix=None, couleur="Blanc", conso=6.0) :
        # Trois attributs d’instance...
        self.marque = marque
        self.annee = annee
        self.modele = modele
        self.prix = prix
        self.couleur = couleur
        self.conso = conso

    def __str__(self):
        # Redéfinition pour le print(instance)...
        return f"Voiture : {self.marque} {self.modele} - {self.annee} - {self.couleur} - {self.conso}L/100km - {self.prix}€"
    # Calcul du nombre de litre de carburant utilisé pour faire une distance
    def calcul_consommation(self, distance) :
        return self.conso * (distance/100)
    def calcul_prix(self, distance) :
        return Voitures.prix_litre * self.calcul_consommation(distance)

    def modif_prix_litre(self, new_prix_litre) :
        Voitures.prix_litre = new_prix_litre


