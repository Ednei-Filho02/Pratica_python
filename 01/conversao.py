"""
Pode haver momentos em que você queira especificar um tipo para uma variável.
Isso pode ser feito com conversão de tipo (casting). Python é uma linguagem orientada a objetos e, como tal, 
usa classes para definir tipos de dados, incluindo seus tipos primitivos.

Em Python, a conversão de tipos é feita usando funções construtoras:

int() - constrói um número inteiro a partir de um literal inteiro, 
um literal de ponto flutuante (removendo todas as casas decimais) ou 
um literal de string (desde que a string represente um número inteiro).

float() - constrói um número float a partir de um literal inteiro, 
um literal float ou um literal de string (desde que a string represente um float ou um inteiro)

str() - constrói uma string a partir de uma ampla variedade de tipos de dados, incluindo strings, 
literais inteiros e literais de ponto flutuante.

"""
# Conversão de tipos
n1 = 10    
n2 = float(n1)  # Converte n1 para float
print(f"O valor de n1 é {n1} e o tipo é {type(n1)}")
print(f"O valor de n2 é {n2} e o tipo é {type(n2)}")   
