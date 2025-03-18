# TEST
class A:
    def __init__(self, arg_A):
        self.attr_A = arg_A
        # Attribut propre à A
        print(f"Initialisation de A (constructeur de 'A') : attribut = {self.attr_A}")
        print("D'après le MRO de 'D', on a terminé de remonter la chaîne des 'super()'...\n")
class B:
    def __init__(self, arg_A, arg_B):  # Ajout de l'argument role
        self.attr_B = arg_B
        # Attribut propre à B
        print(f"Initialisation de B (constructeur de 'B') : attribut = {self.attr_B}")
        print("D'après le MRO de 'D', comme on est dans le constructeur de la classe B,")
        print("\tle prochain 'super()' fait appel au constructeur de la classe A")
        super().__init__(arg_A)  # Appelle la classe suivante dans le MRO
class C(B) :
    def __init__(self, arg_A, arg_B, arg_C):
        self.attr_C = arg_C
        # Attribut propre à C
        print(f"Initialisation de C (constructeur de 'C') : attribut = {self.attr_C}")
        print("D'après le MRO de 'D', comme on est dans le constructeur de la classe C,")
        print("\tle prochain 'super()' fait appel au constructeur de la classe B")
        super().__init__(arg_A, arg_B)  # Appelle la classe suivante dans le MRO

class D(C, A) :
    def __init__(self, arg_A, arg_B, arg_C, arg_D):
        self.attr_D = arg_D
        # Attribut propre à D
        print(f"Initialisation de D (constructeur de 'D') : attribut = {self.attr_D}")
        print("D'après le MRO de 'D', comme on est dans le constructeur de la classe D,")
        print("\tle prochain 'super()' fait appel au constructeur de la classe C")
        super().__init__(arg_A, arg_B, arg_C)  # Appelle la classe suivante du MRO

# Création d'une instance de D
print("On va créer une instance 'd' de la classe 'D'...")
print(f"Le MRO de l'objet D est : {D.__mro__}\n")
d = D("argument_A", "argument_B", "argument_C", "argument_D")