'''
Herança em Python - A herança nos permite definir uma classe que herda todos os métodos e propriedades de outra classe.

A classe pai é a classe da qual a herança é feita, também chamada de classe base.

Uma classe filha é uma classe que herda de outra classe, também chamada de classe derivada.
'''

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

# class Student(Person):
#   def __init__(self, fname, lname): # o adicionar a __init__() função, a classe filha deixará de herdar a __init__() função da classe pai.
#     Person.__init__(self, fname, lname) # Para manter a herança da __init__() função pai, adicione uma chamada à __init__() função pai:

# x = Student("Mike", "Olsen")
# x.printname()



class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)    # Ao usar a super()função, você não precisa usar o nome do elemento pai, 
                                      # pois ele herdará automaticamente os métodos e propriedades do elemento pai.
    self.graduationyear = year

  def printStudent(self):
    print(self.firstname, self.lastname, self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.printStudent()
