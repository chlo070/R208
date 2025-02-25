"""
    consignes:
1. Place dans une liste un nombre aléatoire (entre 10 et 20) d’entiers qui ont eux-mêmes des valeurs aléatoires entre 0 et 100.
2. Dans une boucle « folle », demande à l’utilisateur de donner une valeur d’index de la liste pour afficher ensuite la valeur correspondante dans la liste.

Lors du test de votre script, donnez des valeurs d’index « en-dedans » et « en-dehors » de la liste. Que se passe-t-il ?
3. Modifiez votre code pour intégrer dans la boucle « folle » une structure « try » … « except » qui va gérer une éventuelle « IndexError » de manière à ce que la boucle « folle » ne se termine
jamais… Le message d’erreur doit donner l’intervalle des valeurs d’index possibles…

 que se passe-t-il si vous répondez à la question par un caractère non numérique ?
4. Apportez une nouvelle modification à votre code pour que la boucle « folle » reste « folle »
"""

#1. Place dans une liste un nombre aléatoire (entre 10 et 20) d’entiers qui ont eux-mêmes des valeurs aléatoires entre 0 et 100.
import random

randnum = []
for i in range (random.randint(10,20)) :
    randnum.append(random.randint(0, 100))
while True :
    try :
        ind = int(input(f"Donnez une valeur d'index de la liste : "))



#Correction
#ne pas oublier if__name__ == "__main__" à chaque fois
liste = []
for i in range (random.randint(10,20)) :
    liste.append(random.randint(0,100))
while True :
    try :
        index = int(input(f"Donnez une valeur d'index de la liste : "))
        second_nb = float(input("Entrez un second nombre : "))
        print(f"")
        print(liste.index())
    except IndexError:
        bivug
    except ValueError:
        vcfe
    except ZeroDivisionError :
        fecvr
    except Exception as 0 :
        vfvf
    except Exception as e:  # "Exception" générique
        print(type(e))
#fin correction

