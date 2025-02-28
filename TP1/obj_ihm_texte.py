from obj_voitures import Voitures
import time, re

class Ihm:
    """
    Interface Homme-Machine (IHM) pour la gestion d'une flotte de véhicules.
    """
    def __init__(self, liste_vehicules):
        """
        Constructeur : Initialise l'IHM avec une liste de véhicules.

        :argument liste_vehicules: Liste des objets Voitures.
        """
        self.liste_vehicules = liste_vehicules
        self.choix = 0

    def menu_accueil(self):
        """
        Affiche le menu principal et attend l'entrée de l'utilisateur.
        """
        while True:
            print("\n" * 100)
            print("   _____    ____    _   _    _____   ______    _____    _____   _____    ____    _   _ ")
            print("  / ____|  / __ \  | \ | |  / ____| |  ____|  / ____|  / ____| |_   _|  / __ \  | \ | |")
            print(" | |      | |  | | |  \| | | |      | |__    | (___   | (___     | |   | |  | | |  \| |")
            print(" | |      | |  | | | .  | | |      |  __|    \___ \   \___ \    | |   | |  | | | .  |")
            print(" | |____  | |__| | | |\  | | |____  | |____   ____) |  ____) |  _| |_  | |__| | | |\  |")
            print("  \_____|  \____/  |_| \_|  \_____| |______| |_____/  |_____/  |_____|  \____/  |_| \_|")
            print("\n")
            print("\t1. Lister tous les véhicules.")
            print("\t2. Ajouter un véhicule.")
            print("\t3. Modifier un véhicule.")
            print("\t4. Supprimer un véhicule.")
            print("\t5. Calculer la consommation sur un trajet.")
            print("\t6. Calculer le prix du carburant pour un trajet.")
            print("\t7. Calculer l'impact carbone d'un trajet.")
            print("\t8. Quitter.")
            print("\n" * 2)
            if self.__attendre_choix_ligne(8, "\t--> Choisissez une action (numéro) : "):
                break

    def menu_lister(self):
        """
        Affiche la liste des véhicules et attend la confirmation de l'utilisateur.
        """
        self.__affichage_liste_vehicules()
        tmp = input("\nAppuie sur Entrée pour continuer...")
        self.choix = 0

    def menu_ajouter(self):
        """
        Ajoute un nouveau véhicule en demandant les informations à l'utilisateur.
        """
        print("\n" * 100)
        while True:
            marque = input("\t--> Entrez la marque : ").strip().capitalize()
            if marque == "":
                print("\t************ Erreur : Valeur saisie incorrecte...")
            else:
                break

        # ***********************************
        # Code à COMPLETER....
        # ***********************************

        motif = r"[0-9]{4}"
        while True:
            code = input("\t--> Le code du système audio (nnnn) ? : ").strip()
            if not re.fullmatch(motif, code):
                print("\t************ Erreur : Valeur saisie incorrecte...")
            else:
                break

        # ***********************************
        # ligne à MODIFIER....
        obj_voiture = Voitures(marque, "Blablabla", 2300, "Transparente", 0.0, 0, "0000 0000 0000", code)
        # ***********************************

        print()
        print(f"\t----> Véhicule ajouté : {obj_voiture}")
        print()
        input("\nAppuie sur Entrée pour continuer...")
        self.choix = 0

    def menu_modifier(self):
        """
        Permet de modifier un véhicule existant en choisissant un attribut à modifier.
        """
        while True:
            self.__affichage_liste_vehicules()
            if self.__attendre_choix_ligne(len(self.liste_vehicules), "\t--> Choisissez le véhicule à modifier (numéro) : "):
                num_vehicule = self.choix - 1
                break
        while True:
            try:
                print("\n" * 100)
                print("\t1. La marque.")
                print("\t2. Le modele.")
                print("\t3. L'année.")
                print("\t4. La couleur.")
                print("\t5. La consommation.")
                print("\t6. Le prix.")
                print("\t7. Le numéro de série.")
                print("\t8. Le code du système audio.")
                print("\n" * 2)
                if self.__attendre_choix_ligne(8, "\t--> Choisissez l'attribut à modifier (numéro) : "):
                    changement = input("\t--> Veuillez donner la nouvelle valeur : ").strip()
                    if self.choix == 1:
                        self.liste_vehicules[num_vehicule].marque = changement


                    # ***********************************
                    # Code à COMPLETER....
                    # ***********************************


                    elif self.choix == 8:
                        motif = r"[0-9]{4}"
                        if re.fullmatch(motif, changement):
                            self.liste_vehicules[num_vehicule].set_audio_code(changement)
                        else:
                            raise ValueError
                    print(f"\t----> {self.liste_vehicules[num_vehicule]}")
                    print("\t----> La modification est faite...")
                    tmp = input("\nAppuie sur Entrée pour continuer...")
                    break
            except ValueError:
                print("Erreur : Valeur saisie incorrecte...")
                time.sleep(2)

        self.choix = 0

    def menu_supprimer(self):
        """
        Supprime un véhicule sélectionné par l'utilisateur.
        """

        # ***********************************
        # Code à COMPLETER....
        # ***********************************


        tmp = input("\nAppuie sur Entrée pour continuer...")

        self.choix = 0

    def menu_conso(self):
        """
        Calcule la consommation de carburant d'un véhicule sur une distance donnée.
        """
        while True:
            self.__affichage_liste_vehicules()
            if self.__attendre_choix_ligne(len(self.liste_vehicules), "\t--> Choisissez un véhicule pour le calcul (numéro) : "):
                num_vehicule = self.choix - 1
                break
        dist = int(input(f"\t--> Veuillez entrer la distance (km) d'un trajet : ").strip())
        print(f"\t----> La {self.liste_vehicules[num_vehicule].modele} consomme {self.liste_vehicules[num_vehicule].calcul_consommation(dist)} litres de carburant sur {dist} km...")
        tmp = input("\nAppuie sur Entrée pour continuer...")

        self.choix = 0

    def menu_prix(self):
        """
        Calcule le coût du carburant pour un trajet donné.
        """

        # ***********************************
        # Code à COMPLETER....
        # ***********************************

    def menu_carbone(self):
        """
        Calcule l'empreinte carbone d'un trajet pour un véhicule donné.
        """

        # ***********************************
        # Code à COMPLETER....
        # ***********************************

    def __attendre_choix_ligne(self, choix_maxi, texte):
        """
        Attend et valide l'entrée de l'utilisateur.

        :argument choix_maxi: Nombre maximal de choix possibles.
        :argument texte: Texte affiché pour demander l'entrée.
        :retour: True si choix valide, False sinon.
        """
        try:
            self.choix = int(input(texte))
            if 0 < self.choix <= choix_maxi:
                return True
            else:
                raise ValueError
        except ValueError:
            print("\t************ Erreur : choix invalide...")
            time.sleep(2)
            return False

    def __affichage_liste_vehicules(self):
        """
        Affiche la liste des véhicules disponibles.
        """
        print("\n" * 100)
        print("La listes des véhicules du parc est :")
        for num in range(len(self.liste_vehicules)):
            print(f"\t{num+1}. {self.liste_vehicules[num]}")
        print("\n" * 2)
