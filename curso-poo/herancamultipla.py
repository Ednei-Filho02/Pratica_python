class Animal:
    def __init__(self, apelido):
        print(f"Classe Animal: {apelido}")

class Mamifero(Animal):
    def __init__(self, apelido):
        print(f"Classe Mamifero: {apelido}")
        super().__init__(apelido)

class Naovoadores(Mamifero):
    def __init__(self, apelido):
        print(f"Classe Nao Voadores: {apelido}")
        super().__init__(apelido)

class Naoaquaticos(Mamifero):
    def __init__(self, apelido):
        print(f"Classe Nao Aquaticos: {apelido}")
        super().__init__(apelido)
class Dog(Naoaquaticos, Naovoadores):
    def __init__(self, apelido):
        print(f"Classe Nao Voadores e Nao Aquaticos: {apelido}")
        super().__init__(apelido)


cachorro = Dog("Rex")