"""
Uma função é um bloco de código que só é executado quando é chamado.

Uma função pode retornar dados como resultado.

Uma função ajuda a evitar repetição de código.

"""
# exemplo de função
def saudacao():
    print("Olá, seja bem-vindo(a)!")
    
# chamada da função
saudacao()

# exemplo de função com parâmetro
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")   

# chamada da função com argumento
saudacao("Ednei")


# exemplo de função com retorno
def soma(a, b): 
    return a + b    

# chamada da função com retorno
resultado = soma(5, 3)
print(f"O resultado da soma é: {resultado}")

# exemplo de função com valor padrão
def saudacao(nome="Visitante"):
    print(f"Olá, {nome}! Seja bem-vindo(a)!")       

# chamada da função com valor padrão
saudacao()  # Usando o valor padrão
saudacao("Ednei")  # Passando um argumento  

# exemplo de função com múltiplos parâmetros
def saudacao(nome, idade):
    print(f"Olá, {nome}! Você tem {idade} anos. Seja bem-vindo(a)!")

# chamada da função com múltiplos argumentos
saudacao("Ednei", 30)

# exemplo de função com retorno de múltiplos valores
def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b if b != 0 else None
    return soma, subtracao, multiplicacao, divisao

# chamada da função com retorno de múltiplos valores
resultado = operacoes(10, 5)
print(f"Soma: {resultado[0]}, Subtração: {resultado[1]}," 
      " Multiplicação: {resultado[2]}, Divisão: {resultado[3]}")  

# exemplo de função com argumento arbitrário
def lista_de_nomes(*nomes):
    for nome in nomes:
        print(f"Olá, {nome}! Seja bem-vindo(a)!")       

# chamada da função com argumento arbitrário
lista_de_nomes("Ednei", "Maria", "João")    

# exemplo de função combinando somente posicionamento e somente palavra-chave
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

# exemplo de função com args
def soma_numeros(*args):
    return sum(args)

resultado = soma_numeros(1, 2, 3, 4, 5)
print(f"A soma dos números é: {resultado}")