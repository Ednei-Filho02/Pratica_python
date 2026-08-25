"""
Listas são usadas para armazenar múltiplos itens em uma única variável.

As listas são criadas usando colchetes: [ ]

A lista é editável, o que significa que podemos alterar, adicionar e remover itens de uma lista depois de ela ter sido criada.
A criação de lista vazia pode ser feita com a função list() ou com colchetes vazios: [].

"""
# Exemplo de lista
thislist = ["apple", "banana", "cherry"]
print(thislist)

# Exemplo de como verificar o tamanho da lista
print(len(thislist))

# exemplo de sort e  sort reverse
thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)

# exemplo de sun, min e max
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(numeros)
print(sum(numeros))
print(min(numeros))
print(max(numeros))

# exemplo de append, insert e remove

append_list = [1, 2, 3]
append_list.append(4)   
print(append_list)     


insert_list = [1, 2, 3]
insert_list.insert(1, 1.5)
print(insert_list)


remove_list = [1, 2, 3, 4, 5]
remove_list.remove(3)   

# exemplo de pop
pop_list = [1, 2, 3, 4, 5]
pop_list.pop()  

# exemplo de clear
clear_list = [1, 2, 3, 4, 5]
clear_list.clear()

# exemplo de index
index_list = [1, 2, 3, 4, 5]
print(index_list.index(3))

# exemplo de count
count_list = [1, 2, 3, 4, 5, 3]
print(count_list.count(3))

# exemplo de copy
copy_list = [1, 2, 3, 4, 5]
copy_list = copy_list.copy()
print(copy_list)

# exemplo de extend
extend_list1 = [1, 2, 3]
extend_list2 = [4, 5, 6]
extend_list1.extend(extend_list2)
print(extend_list1)

# exemplo de verificação com in 
check_list = [1, 2, 3, 4, 5]
if 3 in check_list:
    print("3 está na lista e está na posição:", check_list.index(3))
else:
    print("3 não está na lista")

# exemplo de apresentação 
print(check_list[2:])

# exemplo de slicing
slicing_list = [1, 2, 3, 4, 5] 
print(slicing_list[1:4])  # Acessando elementos do índice 1 ao 3 (4 não incluído)

# exemplo de comprehensions
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)  # Saída: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# exemplo de none
none_list = [None, None, None] # o mesmo de criar uma lista vazia, mas com o valor None

# exemplo de in e ==
check_list = [1, 2, 3, 4, 5]
print(3 in check_list)  # Verifica se o valor 3 está na lista
print(3 == check_list[4])  # Verifica se o valor 3 é igual ao elemento no índice 2  
