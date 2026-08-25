"""
Os operadores lógicos são usados ​​para combinar instruções condicionais. Python possui três operadores lógicos:

and- Retorna Verdadeiro se ambas as afirmações forem verdadeiras.
or- Retorna verdadeiro se uma das afirmações for verdadeira.
not- Inverte o resultado, retornando False se o resultado for verdadeiro.

"""

# exemplo de operador lógico and
idade = 20
if idade >= 18 and idade < 65:
    print("Você é um adulto.")

# exemplo de operador lógico or
idade = 10
if idade < 18 or idade >= 65:
    print("Você não é um adulto.")
else:
    print("Você é um adulto.")

# exemplo de operador lógico not
idade = 17
if not idade < 18:
    print("Você é um adulto.")  
else:
    print("Você não é um adulto.")
