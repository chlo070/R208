from obj_couleur import Couleur
from obj_auteur import Auteur(Couleur)

class Livre(Couleur):
    nombre_total_livres = 0    # Création d’une instance.
    def __init__(self, titre, auteur, isbn = None, annee_publication = None):   # Constructeur et ses 4 arguments
        Livre.nombre_total_livres += 1    # Incrémentation de l'instance de classe
        # Six attributs d’instance
        self.id = Livre.nombre_total_livres
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn if isbn else "N/A"
        self.annee_publication = annee_publication if annee_publication else "inconnue"
        if pays == None :
            self.pays = "inconnu"
        if date_naissance == None :
            self.date_naissance = "inconnue"
    def __str__(self):  # Redéfinition pour le print(instance)...
        return f"{Auteur.BLEU}{self.id} {Auteur.NO_COLOR} {self.nom} {self.prenom} {Auteur.MAGENTA}(né(e) le {self.date_naissance} en {self.pays}) {Auteur.NO_COLOR}"


follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
verne = Auteur("VERNE","Jules","France", "08/02/1828")
print("Création de 3 instances de Livre et affichage...")
livre_1 = Livre("Les Piliers de la Terre", follett, "9782130428114", "1989")
livre_2 = Livre("Une Colonne de Feu", follett, "9782221157695", "2017")
livre_2.disponible = False
livre_3 = Livre("Vingt Mille Lieues sous les mers", verne, "9782070364234", "1870")
print(livre_1)
print(livre_2)
print(livre_3)