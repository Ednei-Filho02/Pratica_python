'''
Todas as classes possuem um método embutido chamado __init__(), que é sempre executado 
quando a classe está sendo inicializada.

O __init__()método é usado para atribuir valores às propriedades de um objeto ou para 
executar operações necessárias durante a criação do objeto.
'''
class Person:
  def __init__(self, name, age): # o __init__()método é chamado automaticamente sempre que a classe é 
    self.name = name             # usada para criar um novo objeto.   
    self.age = age

  def greet(self):         # Utilize self para acessar as propriedades da classe:
    print("Hello, my name is " + self.name)

  def oi(self):
    return "hello, " + self.name 

  def welcome(self):
    message = self.oi()   # Chamar um método a partir de outro método usando self:
    print(message + "! Welcome to our website.")

p1 = Person("Ednei", 25) 

print(p1.name, p1.age)
p1.greet()
p1.welcome()


# Adicionar propriedades dessa forma as adiciona apenas a esse objeto específico, não a todos os objetos da classe.
class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name, p1.age, p1.city)


# para remover um propriedade -> del
del p1.city


# Alterar uma propriedade de classe:

class Person:
  lastname = ""  # Propriedade de classe

  def __init__(self, name):
    self.name = name   # propriedade de instância   

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)