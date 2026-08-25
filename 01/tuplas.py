"""
As tuplas são usadas para armazenar múltiplos itens em uma única variável.

Uma tupla é uma coleção ordenada e imutável .

As tuplas são escritas com parênteses ().
Metados de tuplas são limitados, pois não podem ser alteradas depois de criadas.
Com isso os metados pop, remove, clear, sort e reverse não podem ser usados em tuplas.

"""
# exemplo de uma tupla
tupla = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tupla)

# exemplo de como verificar o tamanho da tupla
print(len(tupla))

# exemplo de como acessar elementos da tupla
print(tupla[1])  # Acessando o segundo elemento da tupla

# exemplo de como ordenar uma tupla
tupla_ordenada = sorted(tupla)
print(tupla_ordenada)   # ou somente print(sorted(tupla))