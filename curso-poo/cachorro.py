# -- Definição da classe Cachorro

class Cachorro:
    def __init__(self, apelido, idade, raca):
        print(f"Criando um novo cachorro chamado {apelido}...")
        self.apelido = apelido
        self.idade = idade
        self.raca = raca
    # -- Métodos de instância 
    def sentar(self):
        print(f"{self.apelido} sentou!")

    def rolar(self):
        print(f"{self.apelido} rolou no chão!")

    def correr(self, velocidade="rapidamente"):
        print(f"{self.apelido} está correndo {velocidade}.")

    def comer(self, comida):
        print(f"{self.apelido} está comendo {comida}.")