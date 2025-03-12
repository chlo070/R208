from obj_couleur import Couleur
from obj_auteur import Auteur(Couleur)

class Livre(Couleur):
    nombre_total_livres = 0    # Création d’une instance.
    def __init__(self, titre, auteur, isbn = None, annee_publication = None):   # Constructeur et ses 4 arguments
        Livre.nombre_total_livres += 1    # Incrémentation de l'instance de classe
        # Six attributs d’instance
        self.id = Livre.nombre_total_livres
        self.titre = nom.upper()
        self.auteur = prenom.capitalize()
        self.isbn = pays
        self.annee_publication = annee_publication
        if pays == None :
            self.pays = "inconnu"
        if date_naissance == None :
            self.date_naissance = "inconnue"
    def __str__(self):  # Redéfinition pour le print(instance)...
        return f"{Auteur.BLEU}{self.id} {Auteur.NO_COLOR} {self.nom} {self.prenom} {Auteur.MAGENTA}(né(e) le {self.date_naissance} en {self.pays}) {Auteur.NO_COLOR}"


