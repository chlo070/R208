from obj_couleur import Couleur

class Auteur(Couleur):
    nombre_total_auteurs = 0
    def __init__(self, nom, prenom, pays = None, date_naissance = None):
        Auteur.nombre_total_auteurs += 1
        self.id = Auteur.nombre_total_auteurs
        self.nom = nom
        self.prenom = prenom
        self.pays = pays if pays else "Inconnu"
        self.date_naissance = date_naissance if date_naissance else "Inconnue"
    def __str__(self):  # Redéfinition pour le print(instance)...
        return f"{self.id} {self.nom} {self.prenom} {self.pays} {self.date_naissance}"

print("Création de 3 instances de Auteur et affichage...")
follett = Auteur("FOLLETT", "Ken", "Pays de Galles", "05/06/1949")
verne = Auteur("VERNE","Jules","France", "08/02/1828")
bridou = Auteur("BRIDOU", "Justin", None, None)
print(follett)
print(verne)
print(bridou)
print(bridou.pays)
print(bridou.date_naissance)
