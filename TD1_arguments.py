import sys

if __name__ == '__main__':
    print(sys.argv[0])

    if len(sys.argv) == 1 :
        print('Aucun argument après le nom du script : ', sys.argv[0])

    for i in range(len(sys.argv)): # Boucle avec index…
        print(sys.argv[i])
###
#    for argument in sys.argv: # Boucle avec élément de la liste…
#        print(argument)
###
