import sys
from pathlib import Path

print("bonjour")
if __name__ == '__main__':

    print(sys.argv[0])

    if len(sys.argv) < 2 :
        print(f'Aucun argument après le nom du script : {sys.argv[0]}')
    else :
        for i in range(1, len(sys.argv)) :
            print(f'\t--> {sys.argv[i]}')


##    for i in range(len(sys.argv)): # Boucle avec index…
#      print(sys.argv[i])

#    for argument in sys.argv: # Boucle avec élément de la liste…
#        print(argument)

