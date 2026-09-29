# Classe pai
class ClassePai:
    def __init__(self, atributo):
        self.atributo = atributo
    def metodo_pai(self):
        return "Método da classe pai"

# Classe filha herda de ClassePai
class ClasseFilha(ClassePai):
    def __init__(self, atributo, novo_atributo):
        super().__init__(atributo) # Chama construtor da classe pai
        self.novo_atributo = novo_atributo
    def metodo_filha(self):
        return "Método da classe filha"

# Uso
obj = ClasseFilha("valor1", "valor2")
print(obj.metodo_pai()) # Herdado da classe pai
print(obj.metodo_filha()) # Próprio da classe filha