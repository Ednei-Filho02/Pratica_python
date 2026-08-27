'''
Em Python, o decorador @property transforma um método de classe em um atributo de leitura. 
Ele permite acessar o valor de um método sem usar parênteses no final (objeto.valor em vez 
de objeto.valor()), facilitando cálculos sob demanda e validações sem mudar a interface pública do objeto.

Para que serve -> 
Acesso limpo: Elimina a necessidade de criar métodos get_nome() e set_nome() tradicionais.

Atributos calculados: Permite calcular valores na hora com base em outros dados da classe.

Validação de dados: Controla o que acontece quando um valor é lido, alterado ou apagado por meio de setters e deleters.

Como funciona ->
Getter: Usa @property para definir como o valor é exibido.
Setter: Usa @propriedade.setter para validar e definir um novo valor.

'''

class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        # O sublinhado (_) indica que o atributo é privado por convenção
        self._saldo = saldo_inicial  

    # GETTER: Permite ler o saldo como se fosse um atributo comum
    @property
    def saldo(self):
        return self._saldo

    # SETTER: Protege o saldo contra alterações inválidas
    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo < 0:
            raise ValueError("O saldo não pode ser negativo!")
        self._saldo = novo_saldo


# Criando a conta
conta = ContaBancaria("Alice", 1000)

# Acessando o saldo sem usar parênteses ()
print(conta.saldo)  # Saída: 1000

# Alterando o saldo de forma natural
conta.saldo = 1500
print(conta.saldo)  # Saída: 1500

# Tentando definir um saldo inválido (vai disparar o ValueError)
conta.saldo = -50  # Erro: O saldo não pode ser negativo!