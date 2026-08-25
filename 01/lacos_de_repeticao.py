# Python possui dois comandos de loop primitivos:
# while loops
# for loops

# exemplo de loop while
contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Incrementa o contador em 1

# exemplo de loop while com break
contador = 0
while contador < 10:
    print(contador)
    contador += 1
    if contador == 5:
        break  # Sai do loop quando o contador atingir 5

# exemplo de loop while com continue
contador = 0
while contador < 10:
    contador += 1
    if contador == 5:
        continue  # Pula a iteração quando o contador atingir 5
    print(contador)

# exemplo de loop while com else
contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("Loop while concluído sem interrupção")


# exemplo de loop for
for i in range(5):  # range(5) gera uma sequência de números de
    # 0 a 4 (5 não é incluído)
    print(i)

# exemplo de loop for com strings
frutas = ["maçã", "banana", "cereja"]
for fruta in frutas:
    print(fruta)

# exemplo de loop for aninhados
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

        
 # exemplo de loop for em uma palavra
palavra = "Python"
for letra in palavra:
    print(letra)    