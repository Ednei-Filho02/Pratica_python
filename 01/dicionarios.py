'''
Os dicionários são usados para armazenar valores de dados em pares chave:valor.

Um dicionário é uma coleção ordenada, modificável e que não permite duplicados.

(A partir da versão 3.7 do Python, os dicionários são ordenados . No Python 3.6 e versões anteriores, 
os dicionários não são ordenados .)

Os dicionários são escritos com chaves e possuem chaves e valores:
'''
# exemplo de dicionário
meu_dicionario = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}
print(meu_dicionario)

# exemplo de como acessar elementos do dicionário
print(meu_dicionario["marca"])  # Acessando o valor da chave "marca"

# exemplo de como adicionar elementos ao dicionário
meu_dicionario["cor"] = "vermelho"  # Adicionando uma nova chave-valor
print(meu_dicionario)

# exemplo de como remover elementos do dicionário
del meu_dicionario["ano"]  # Removendo a chave "ano" e seu valor
print(meu_dicionario)   

# exemplo de como verificar o tamanho do dicionário
print(len(meu_dicionario))  # Retorna o número de pares chave-valor

# exemplo de como interar sobre um dicionário
for chave, valor in meu_dicionario.items():
    print(f"Chave: {chave}, Valor: {valor}")    

# exemplo de como adicionar múltiplos elementos ao dicionário
meu_dicionario.update({"ano": 2021, "preco": 30000})  # Adicionando múltiplos pares chave-valor
print(meu_dicionario)   

# exemplo de dicionario aninhado
meu_dicionario_aninhado = {
    "carro1": {
        "marca": "Ford",
        "modelo": "Mustang",
        "ano": 1964
    },
    "carro2": {
        "marca": "Chevrolet",
        "modelo": "Camaro",
        "ano": 1969
    }
}
print(meu_dicionario_aninhado)

# exemplo de como acessar elementos do dicionário aninhado
print(meu_dicionario_aninhado["carro1"]["marca"])  # Acessando o valor da chave "marca" do carro1
print(meu_dicionario_aninhado["carro2"]["modelo"])  # Acessando o valor da chave "modelo" do carro2
