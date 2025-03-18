# Classe Parent
class Animal :
    def __init__(self, nom, age) :   # Constructeur et ses 2 arguments
        # Deux attributs d’instance / instanciation
        self.nom = nom
        self.age = age
    def se_presenter(self):
        print(f"Je me nomme {self.nom}, j’ai {self.age} ans…")
"""
# 1e Test
animaux = [Animal("Simba", 5), Animal("Beethoven", 3), Animal("César", 26), Animal("Dumbo", 1)]
for animal in animaux:
    animal.se_presenter()
"""

# 1e classe Enfant
class Mammifere(Animal) :
    # Constructeur et ses cinq arguments
    def __init__(self, nom, age, race, type_pelage, couleur):
        # Trois nouveaux attributs d’instance
        self.race = race
        self.type_pelage = type_pelage
        self.couleur = couleur
        super().__init__(nom, age) # Les deux 'anciens' attributs d'instance
    # Nouvelle méthode
    def se_presenter(self):
        super().se_presenter()
        print(f"Je suis un(e) {self.race} revêtu de {self.type_pelage} de couleur : {self.couleur}.")
"""
# 2e Test
animaux = [Mammifere("Simba", 5, "lion", "poils courts", "fauve clair"),
Mammifere("Beethoven", 3, "chien", "poils longs", "blanche & fauve"),
Mammifere("César", 26, "singe", "poils courts", "marron"),
Mammifere("Dumbo", 1, "éléphanteau", "peau nue", "grise")]
for animal in animaux:
    animal.se_presenter()
"""

# 2e classe Enfant
class Oiseau(Animal) :
    def __init__(self, nom, age, ordre, envergure):
        # Deux nouveaux attributs d’instance
        self.ordre = ordre
        self.envergure = envergure
        super().__init__(nom, age) # Les deux 'anciens' attributs d'instance
    def se_presenter(self):
        print(f"Je suis un oiseau de type {self.ordre} et mon envergure est de {self.envergure} cm.")
        super().se_presenter()
"""
# 3e Test
animaux = [ Mammifere("Simba", 5, "lion", "poils courts", "fauve clair"), 
Mammifere("Beethoven", 3, "chien", "poils longs", "blanche & fauve"), 
Mammifere("César", 26, "singe", "poils courts", "marron"), 
Mammifere("Dumbo", 1, "éléphanteau", "peau nue", "grise"), 
Oiseau("Hedwige", 7, "rapace", 90), 
Oiseau("Blu", 5, "perroquet", 100), 
Oiseau("Lago", 12, "perroquet", 60), 
Oiseau("Zazu", 40, "passereau", 40)]

for animal in animaux:
    animal.se_presenter()
"""

#   Activité complémentaire
class Personnage :
    def __init__(self, titre, style ="film") :
        self.style = style
        self.titre = titre
    def se_presenter(self):
        print(f"Je joue dans le {style} : {titre}.")

class ActeurMammifere(Mammifere, Personnage) :
    super().__init__()
    print(ActeurMammifere.__mro__)  # connaitre le MRO
class ActeurOiseau(Oiseau, Personnage)
    super().__init__()
