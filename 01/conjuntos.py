'''
Os conjuntos são usados para armazenar vários itens em uma única variável.

Um conjunto é uma coleção que não é ordenada , imutável e não indexada

Os itens definidos não podem ser alterados, mas você pode remover itens e adicionar novos itens.

Para criar um conjunto, use a função set() ou chaves {}.
'''
# exemplo de conjunto
conjunto = {"apple", "banana", "cherry"}
print(conjunto)

# exemplo de como verificar o tamanho do conjunto
print(len(conjunto))

# exemplo de como interar sobre um conjunto
for item in conjunto:
    print(item)

# exemplo de como adicionar elementos a um conjunto
conjunto.add("orange")
print(conjunto)

# exemplo de como remover elementos de um conjunto
conjunto.remove("banana") # caso não exista o elemento, gera um erro
print(conjunto)

# exemplo de como remover elementos de um conjunto com discard
conjunto.discard("cherry") # pode usar o metado pop para fazer a remoção tambem, mas vai ficar aleatório, pois não é indexado
print(conjunto)

# exemplo de adicionar múltiplos elementos a um conjunto
conjunto.update(["kiwi", "melon"])
print(conjunto)

# exemplo de como limpar um conjunto
conjunto.clear()
print(conjunto)

# exemplo de como deletar um conjunto
del conjunto

# exemplo de como verificar se um item está em um conjunto
print("apple" in conjunto)  
