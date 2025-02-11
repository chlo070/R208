import sys
from pathlib import Path

if __name__ == '__main__':

#vérification du nombre d'arguments
    if len(sys.argv) < 5 :
        print("Erreur : Nombre d'arguments insuffisant")
        print("Utilisation : python db_moy.py nom_fichier.txt NOM Prenom note x2")
        sys.exit(1)
    fichier = sys.argv(1)
    f_path =
    f_path = f_path.resolve()
    prenom = sys.argv[3].capitalize()
    notes = sys.argv[4:]

    total = 0.0
    for notes in notes :
        total += float(notes)
    moyenne = total / len(notes)
    else :



#upper(),capitalize(), [0]9.9
#arg1 = le nom du fichier dans lequel on va enregistrer les arguments suivants