from obj_couleur import Couleur
from obj_auteur import Auteur
from obj_livre import Livre

class Membre(Couleur):
    nombre_total_membres = 0    # Création d’une instance.
    def __init__(self, nom, prenom, date_naissance):   # Constructeur et ses 3 arguments
        Membre.nombre_total_membres += 1    # Incrémentation de l'instance de classe
        # Cinq attributs d’instance / instanciation
        self.id = Membre.nombre_total_membres
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.livres_empruntes = ()
    def __str__(self):  # Redéfinition pour le print(instance)...
        return (f"{Membre.BLEU}{self.id}.\t :{Membre.NO_COLOR}{self.prenom} {self.nom} {Membre.MAGENTA}(né(e) le {self.date_naissance})")

if __name__ == "__main__":
    print("Création de 2 instances de Membre et affichage...")
    albert = Membre("EINSTEIN", "Albert", "14/03/1879")
    marie = Membre("CURIE", "Marie", "07/11/1867")
    print(albert)
    print(marie)
    #  Ajout d'une méthode
    follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
    # Livres avec l'instance de leur auteur
    livre_1 = Livre("Les Piliers de la Terre", follett, "9782130428114", "1989")
    livre_2 = Livre("Une Colonne de Feu", follett, "9782221157695", "2017")
    # Test ajout des emprunts "à la main"
    albert.livres_empruntes.append(livre_1)
    albert.livres_empruntes.append(livre_2)
    print("\n*** 1er affichage des livres empruntés...")
    albert.lister_emprunts()
    marie.lister_emprunts()
    "/// Marie CURIE n'a aucun livre emprunté." if None else