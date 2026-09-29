"""
#--- Definição da Classe Pessoa
class Pessoa:

    def __init__(self, nome, idade):
        """"""Inicializa os atributos que descrevem uma pessoa.
        self.nome = nome
        self._idade = idade # <------ Inserido um underscore para indicar atributo fracamente privado.

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self._idade # <------ Retornando um atributo fracamente privado.

nova_pessoa = Pessoa('Carlos Alberto', 80)
print(nova_pessoa.nome)
print(nova_pessoa._idade) # <------ Exibindo um atributo fracamente privado. Pode acessar diretamente, mas não é o recomendado.
print(nova_pessoa.get_idade()) # <------ Exibindo um atributo fracamente privado por meio do método get().


"""
#--- Definição da Classe Pessoa
class Pessoa:

    def __init__(self, nome, idade):
        """Inicializa os atributos que descrevem uma pessoa."""
        self.nome = nome
        self.__idade = idade # <------ Inserido dois underscores para indicar atributo fortemente privado.

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.__idade # <------ Retornando um atributo fortemente privado.

nova_pessoa = Pessoa('Carlos Alberto', 80)
print(nova_pessoa.nome)
print(f'Idade = {nova_pessoa.get_idade()}.') # <------ Exibindo um atributo fortemente privado.
print(nova_pessoa._Pessoa__idade) # <------ Exibindo um atributo fortemente privado por meio da classe.