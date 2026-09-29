class Animal:
    """Classe base para todos os animais"""
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def emitir_som(self):
        return "Som genérico de animal"
    def informacoes(self):
        return f"{self.nome}, {self.idade} anos"

class Cachorro(Animal):
    """Cachorro herda de Animal"""
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade) # Chama __init__ de Animal
        self.raca = raca
    def emitir_som(self):
        return "Au au!"
    def abanar_rabo(self):
        return f"{self.nome} está abanando o rabo"

class Gato(Animal):
    """Gato herda de Animal"""
    def __init__(self, nome, idade, cor_pelo):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo
    def emitir_som(self): # Sobreescreve o metodo 
        return "Miau!"
    def arranhar(self):
        return f"{self.nome} está arranhando"

# Demonstração do uso das classes e herança
rex = Cachorro("Rex", 5, "Labrador")
mimi = Gato("Mimi", 3, "Preto")

print(f"{rex.informacoes()}") # Herdado de Animal. Rex, 5 anos
print(f"Som: {rex.emitir_som()}") # Sobrescrito em Cachorro. Som: Au au!
print(f"{rex.abanar_rabo()}") # Específico de Cachorro. Rex está abanando o rabo

print(f"\n{mimi.informacoes()}") # Herdado de Animal. Mimi, 3 anos
print(f"Som: {mimi.emitir_som()}") # Sobrescrito em Gato. Som: Miau!
print(f"{mimi.arranhar()}") # Específico de Gato. Mimi está arranhando