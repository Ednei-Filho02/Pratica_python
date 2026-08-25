"""

Python suporta as condições lógicas usuais da matemática:

Igual a: a == b
Diferente de: a != b
Menor que: a < b
Menor ou igual a: a <= b
Maior que: a > b
Maior ou igual a: a >= b
Essas condições podem ser usadas de diversas maneiras, mais comumente em instruções "if" e em loops.

Uma "declaração condicional" é escrita usando a palavra-chave if .

"""

# Exemplos de condicional if, else e elif
idade = 18  
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 13:
    print("Você é um adolescente.")
else:
    print("Você é menor de idade.") 

nota = 7.5
if nota >= 7:
    print("Aprovado!")  
elif nota >= 5:
    print("Recuperação!")   
else:
    print("Reprovado!")


# Exemplo de condicional aninhada
idade = 20
if idade >= 18:
    print("Você é maior de idade.")
    if idade >= 65:
        print("Você é um idoso.")
    else:
        print("Você é um adulto.")

# Exemplo de condição if e else em uma linha 
idade = 20 
print("Você é maior de idade.") if idade >= 15 else print("Você não é maior de idade.")