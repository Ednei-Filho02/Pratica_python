'''
A palavra "polimorfismo" significa "muitas formas" e, em programação, 
refere-se a métodos/funções/operadores com o mesmo nome que podem ser executados em vários objetos ou classes.

'''

# Polimorfismo de função

# Um exemplo de função em Python que pode ser usada em diferentes objetos é a len() função.

# Para strings, len()retorna o número de caracteres:
x = "Hello World!"

print(len(x))

# Para tuplas, len()retorna o número de itens na tupla:
mytuple = ("apple", "banana", "cherry")

print(len(mytuple))

# Para dicionários, len()retorna o número de pares chave/valor no dicionário:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))


# Polimorfismo de Classe - O polimorfismo é frequentemente usado em métodos de classe, onde podemos ter várias classes com o mesmo nome de método.
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1): # Observe o laço `for` no final. Devido ao polimorfismo, podemos executar o mesmo método para todas as três classes.
  x.move()

# Polimorfismo de Classe de Herança

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

'''
As classes filhas herdam as propriedades e os métodos da classe pai.

No exemplo acima, você pode ver que a Carclasse está vazia, mas ela herda brand, model, e move()de Vehicle.

As classes ` BoatA` e ` B` Planetambém herdam de `A` brand, model`B` e move()`C` Vehicle, mas ambas sobrescrevem o move() método.

Graças ao polimorfismo, podemos executar o mesmo método para todas as classes.
'''