'''
Um método estático em Python é uma função dentro de uma classe que 
não precisa de uma instância (objeto) nem da própria classe para funcionar

O que é e como funciona:

Sem self ou cls: Diferente dos métodos normais, ele não recebe o argumento 
self (que aponta para o objeto) ou cls (que aponta para a classe).

Decorador @staticmethod: É criado usando esse comando logo acima da função
para avisar ao Python que se trata de um método estático.

Pode ser chamado direto pelo nome da classe, sem precisar criar um objeto dela.

Para que serve:

Funções utilitárias: Ajuda a guardar funções que ajudam a classe, mas que só 
fazem uma tarefa isolada (como um cálculo matemático).

Organização: Mantém o código arrumado e agrupado por temas dentro da classe certa

'''

#Exemplo simples:
class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b

# Chamando sem criar instância da classe
resultado = Matematica.somar(2, 3)  
print(resultado)
