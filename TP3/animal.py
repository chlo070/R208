
class Animal :
    def __init__(self, nom, age) :   # Constructeur et ses 2 arguments
        # Deux attributs d’instance / instanciation
        self.nom = nom
        self.age = age
    def se_presenter(self):
        print(f"Je me nomme {self.nom}, j’ai {self.age} ans…")

# Test
animaux = [Animal("Simba", 5), Animal("Beethoven", 3), Animal("César", 26), Animal("Dumbo", 1)]

for animal in  animaux:
    animal.se_presenter()

class Mammifere(Animal) :
    #Constructeur et ses cinq arguments
    def afficher(self, nom, age, race, type_pelage, couleur):
        # Cinq attributs d’instance
        self.nom = nom
        self.age = age
        self.race = race
        self.type_pelage = type_pelage
        self.couleur = couleur

# Test
animaux = [Mammifere("Simba", 5, "lion", "poils courts", "fauve clair"),
Mammifere("Beethoven", 3, "chien", "poils longs", "blanche & fauve"),
Mammifere("César", 26, "singe", "poils courts", "marron"),
Mammifere("Dumbo", 1, "éléphanteau", "peau nue", "grise")]