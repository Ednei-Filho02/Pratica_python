'''
Funções Lambda para Ações Rápidas: Funções anônimas de uma única linha facilitam a declaração de lógicas rápidas 
e temporárias, eliminando a verbosidade de definir funções completas via def para operações simples.

Transformação e Filtragem Eficientes com Map e Filter: O map() permite aplicar transformações em coleções inteiras,
enquanto o filter() simplifica a exclusão de itens que não atendem a condições lógicas específicas, gerando objetos 
de memória otimizada (generators) no Python 3.

Agrupamento Posicional Dinâmico com Zip: A função zip() possibilita iterar em paralelo sobre múltiplos 
conjuntos de dados de forma pareada, oferecendo recursos inteligentes para o desempacotamento e transposição 
de estruturas multidimensionais.

Controle Elegante de Iteração com Enumerate: O enumerate() resolve de forma definitiva o problema clássico 
de rastrear o índice numérico e o valor dos itens durante um loop, eliminando variáveis contadoras manuais 
que poluem o código.

'''
# estrutura -> lambda parâmetros: resultado
# exemplo de funções Lambda

# Com função normal
def dobrar(x):
    return x * 2

print(dobrar(5))


# com lambda
dobrar = lambda x: x * 2

print(dobrar(5))

# exemplo 2
maior = lambda a, b: a if a > b else b

print(maior(10, 15))


# map() — transformar vários valores
# Exemplo 1

precos = [100, 200, 300, 400]

novos_precos = list(map(lambda x: x * 0.9, precos))

print(novos_precos)

# exemplo 1 - sem map()

novos_precos = []

for preco in precos:
    novos_precos.append(preco * 0.9)

print(novos_precos)


# filter() — filtrar valores ou seja filter() = "quero somente os elementos que atendem a uma condição".
# Exemplo de filter() 

idades = [12, 17, 18, 21, 15, 30]

maiores = list(filter(lambda idade: idade >= 18, idades))

print(maiores)


# enumerate() — pegar índice + valor
# Exemplo 

alunos = ["João", "Maria", "Pedro"]

for indice, aluno in enumerate(alunos): # enumerate(alunos, start=1): -> fazer começar a conta em 1
    print(indice, aluno)

# zip() — juntar listas 
# Exemnplo 1

nomes = ["João", "Maria", "Pedro"]
idades = [20, 25, 30]

for nome, idade in zip(nomes, idades):
    print(nome, idade)

# Exemplo 2

produtos = ["Mouse", "Teclado", "Monitor"]
precos = [50, 100, 800]

for produto, preco in zip(produtos, precos):
    print(f"{produto}: R${preco}")