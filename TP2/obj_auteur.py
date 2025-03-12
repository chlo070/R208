from obj_couleur import Couleur

class Auteur(Couleur):
    nombre_total_auteurs = 0    # Création d’une instance.
    def __init__(self, nom, prenom, pays = None, date_naissance = None):   # Constructeur et ses 4 arguments
        Auteur.nombre_total_auteurs += 1    # Incrémentation de l'instance de classe
        # Cinq attributs d’instance
        self.id = Auteur.nombre_total_auteurs
        self.nom = nom.upper()
        self.prenom = prenom.capitalize()
        self.pays = pays
        self.date_naissance = date_naissance
        if pays == None :
            self.pays = "inconnu"
        if date_naissance == None :
            self.date_naissance = "inconnue"
    def __str__(self):  # Redéfinition pour le print(instance)...
        return f"{Auteur.BLEU}{self.id} {Auteur.NO_COLOR} {self.nom} {self.prenom} {Auteur.MAGENTA}(né(e) le {self.date_naissance} en {self.pays}) {Auteur.NO_COLOR}"

if __name__ == "__main__":
    print("Création de 3 instances de Auteur et affichage...")
    follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
    verne = Auteur("VERNE", "Jules", "France", "08/02/1828")
    bridou = Auteur("BRIDOU", "Justin", None, None)
    print(follett)
    print(verne)
    print(bridou)
    print(bridou.pays)
    print(bridou.date_naissance)

