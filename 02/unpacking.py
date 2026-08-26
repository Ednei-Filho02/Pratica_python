'''
desempacotar listas e dicionarios
'''


"""Utilizado em lista para desempacotar os elementos de uma lista e passá-los como argumentos para uma função.
O operador * é usado para desempacotar os elementos de uma lista ou tupla e passá-los como argumentos separados
para uma função.Isso é útil quando você tem uma lista de valores que deseja passar como argumentos para uma função
que espera múltiplos parâmetros. Por exemplo, considere a seguinte função que soma quatro números:"""
def soma(a, b, c, d):
    return a + b + c + d

lista = [1, 2, 3, 10]

print(soma(*lista))  # Desempacotando a lista e passando os elementos como argumentos para a função 


v1, v2, v3, v4 = lista  # Desempacotando a lista em variáveis individuais
print(v1)
print(v2)
print(v3)
print(v4)



v1, *v2, v3 = lista  
print(v1)
print(v2)
print(v3)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = [*list1, 'sei lá' , *list2]  # Desempacotando as duas listas e combinando em uma nova lista
print(combined_list)  # Saída: [1, 2, 3, 'sei lá', 4, 5, 6]


def my_sun(*args): # -> Utiliza o *args quando não souber quantos argumentos serão passados ​​para sua função
    result = 0      # Dessa forma, a função receberá uma tupla de argumentos e poderá acessar os itens de acordo
    for param in args:
        result += param
    return result

print(my_sun(1, 2, 3, 4, 5))  # Saída: 15


"""
Para uso em dicionários, o operador ** é usado para desempacotar os elementos de um dicionário e passá-los 
como argumentos nomeados para uma função. Isso é útil quando você tem um dicionário de valores que deseja
passar como argumentos nomeados para uma função que espera múltiplos parâmetros. 

"""
def my_print(name, age, job):
    print(f"Nome: {name}, Idade: {age}, Profissão: {job}")

dict1 = {"name": "Ednei", "age": 25, "job": "Desenvolvedor"}

my_print(**dict1)  # Desempacotando o dicionário e passando os elementos como argumentos nomeados para a função  

dict2 = {"altura": "1.75", "peso": "70kg"}

combined_dict = {**dict1, **dict2}  # Desempacotando os dois dicionários e combinando em um novo dicionário
print(combined_dict)  # Saída: {'name': 'Ednei', 'age': 25, 'job': 'Desenvolvedor', 'altura': '1.75', 'peso': '70kg'}


def my_function(**kwargs): # -> Utiliza o **kwargs ão souber quantos argumentos nomeados serão passados ​​para sua função
    print('Teste de parametros') # Dessa forma, a função receberá um dicionário de argumentos e poderá acessar os itens de acordo.  
    for k, v in kwargs.items():
        print(f'Parameter Name: {k}, Paramater Value: {v}')


my_function(name='Ednei', test='Diaa', other='Noite' )
