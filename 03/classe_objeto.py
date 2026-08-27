'''
Python é uma linguagem de programação orientada a objetos.

Em Python, quase tudo é um objeto, com suas propriedades e métodos.

Uma classe é como um construtor de objetos, ou um "modelo" para criar objetos.

'''
class MyClass:
    x=5

p1 = MyClass()
print(p1.x)

# Para excuir um objeto -> del

del p1

# Criando vario objetos da mesma classe
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)