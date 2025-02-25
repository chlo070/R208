
"""
    Consignes :
9. Modifiez l’analyse des arguments.
10. Modifiez les messages d’erreur qui indique l’usage du script.
11. Modifiez l’affichage suivant la présence ou non de l’argument facultatif.
"""
"""
    Exemple utilisation d'instruction "exit" :
import sys
if len(sys.argv) < 3: # Arguments insuffisants
print("message d’erreur...")
exit(1) # Arrêt exécution
flag_verbose = False
if len(sys.argv) == 4: # Si argument facultatif présent
if sys.argv[3] != "-v": # Si argument facultatif != -v
print("message d’erreur...")
exit(1) # Arrêt exécution
flag_verbose = True
mot_cle = sys.argv[2] # Traitement des arg. non facultatifs
..........
"""