import sys
from pathlib import Path

# Code du programme principal


"""
PARTIE 1
1. Vérifiez que 2 arguments sont fournis (après le nom du script). Sinon, message d’erreur du type : 
# syntaxe --> usage : extract_log.py nom_fichier.log mot_cle
2. Convertissez le 1er argument en objet « Path » et ajoutez-lui le chemin complet.
3. Vérifiez que le fichier existe bien. Sinon, message d’erreur…
4. Vérifiez que le fichier est réellement un fichier et non un répertoire. Sinon, message d’erreur…
5. Vérifiez que le 2ème argument est bien dans la liste des 3 catégories de messages possibles : 
["ERROR", "WARNING", "INFO"]. Sinon, message d’erreur…
6. Ouvrez le fichier en lecture.
7. Parcourez-le ligne par ligne et chercher le mot clé… Comptez les lignes où figurent le mot clé. 
Note : L’affichage des lignes n’est pas demandé !!!
8. Affichez le compteur de ligne à la fin et comme ceci : 
Le nombre de lignes contenant XXXXX est : nnnnn
"""


