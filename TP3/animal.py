
class Parent:
    def se_presenter(self, nom, age) :   # Constructeur et ses 2 arguments
        # Deux attributs d’instance / instanciation
        self.nom = nom
        self.age = age

animaux = [Animal("Simba", 5), Animal("Beethoven", 3), Animal("César", 26), Animal("Dumbo", 1)]

for animal in  animaux:
    animal.se_presenter()


class Mammifère:
def afficher(self):