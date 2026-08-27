'''
Métodos são funções que pertencem a uma classe. 
Eles definem o comportamento dos objetos criados a partir dessa classe

obs ->   Todos os métodos devem ter 'self' como primeiro parâmetro

Os métodos podem acessar e modificar propriedades de objetos usando self

O __str__() método é um método especial que controla o que é retornado quando o objeto é impresso

Você pode excluir métodos de uma classe usando a 'del' palavra-chave
'''

# class Person:
#   def __init__(self, name):  -> metodo
#     self.name = name

#   def greet(self):           -> metodo 
#     print("Hello, my name is " + self.name)

# p1 = Person("Emil")
# p1.greet()


#Os métodos podem aceitar parâmetros da mesma forma que as funções comuns 
class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))  

# Exemplo de mudar propriedade por metodo
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()

# Exemplo utilizando o metodo __str__()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)