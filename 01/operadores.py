# Os operadores são usados ​​para realizar operações em variáveis ​​e valores.

n1 = 10
n2 = 2

# operador de adição 
soma = n1 + n2
print(f"A soma de {n1} e {n2} é {soma}")

# Operador de subtração
subtracao = n1 - n2 
print(f"A subtração de {n1} e {n2} é {subtracao}")

# Operador de multiplicação
multiplicacao = n1 * n2    
print(f"A multiplicação de {n1} e {n2} é {multiplicacao}")

# Operador de divisão
divisao = n1 / n2 
print(f"A divisão de {n1} e {n2} é {divisao}")

# Operador de divisão inteira
divisao_inteira = n1 // n2 
print(f"A divisão inteira de {n1} e {n2} é {divisao_inteira}")

# Operador de módulo
modulo = n1 % n2
print(f"O módulo de {n1} e {n2} é {modulo}")

# Operador de exponenciação
exponenciacao = n1 ** n2
print(f"A exponenciação de {n1} e {n2} é {exponenciacao}")

# Operadores de comparação
print(f"{n1} é igual a {n2}? {n1 == n2}") # Igual a
print(f"{n1} é diferente de {n2}? {n1 != n2}") # Diferente de
print(f"{n1} é maior que {n2}? {n1 > n2}")  # Maior que
print(f"{n1} é menor que {n2}? {n1 < n2}")  # Menor que
print(f"{n1} é maior ou igual a {n2}? {n1 >= n2}") # Maior ou igual a          
print(f"{n1} é menor ou igual a {n2}? {n1 <= n2}") # Menor ou igual a

# Operadores lógicos
print(f"{n1} > 5 and {n2} < 5? {n1 > 5 and n2 < 5}") # E
print(f"{n1} > 5 or {n2} < 5? {n1 > 5 or n2 < 5}")  # Ou
print(f"not({n1} > 5)? {not(n1 > 5)}")       # Não

# Operadores de atribuição
n1 += 5 # n1 = n1 + 5
print(f"O valor de n1 após a atribuição é {n1}")

# Operadores de identidade
x = ["maçã", "banana"]
y = ["maçã", "banana"]
print(f"{x} is {y}? {x is y}") # False, pois x e y são objetos diferentes
z = x
print(f"{x} is {z}? {x is z}") # True, pois z é uma referência ao mesmo objeto que x
