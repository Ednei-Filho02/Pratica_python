'''
O encapsulamento consiste em proteger os dados dentro de uma classe.

Significa manter dados (propriedades) e métodos juntos em uma classe, 
controlando ao mesmo tempo como os dados podem ser acessados de fora da classe.

Isso evita alterações acidentais nos seus dados e oculta os detalhes internos de como sua classe funciona. 

O encapsulamento oferece diversas vantagens:

Proteção de dados: Impede a modificação acidental de dados
Validação: Você pode validar os dados antes de defini-los.
Flexibilidade: a implementação interna pode ser alterada sem afetar o código externo.
Controle: Você tem controle total sobre como os dados são acessados e modificados.
'''

# Propriedades privadas -> Em Python, você pode tornar propriedades privadas usando um __prefixo com dois sublinhados
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # propriedade privada 


  def get_age(self): # -> para ter acesso ao dado privado
    return self.__age

  def set_age(self, age): # -> para fazer alteração de um dado privado
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

# p1 = Person("Emil", 25)
# print(p1.name)
# print(p1.__age) # Observação: Propriedades privadas não podem ser acessadas diretamente de fora da classe.

p1 = Person("Tobias", 25)
print(p1.get_age())

p1.set_age(26)
print(p1.get_age())

# Propriedade Protegida -> Python também possui uma convenção para propriedades protegidas usando um único _prefixo de sublinhado:
# obs -> Um único sublinhado _é apenas uma convenção. 
# Ele indica a outros programadores que a propriedade se destina ao uso interno, mas o Python não impõe essa restrição.
class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary # propriedade protegida

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary) # Pode acessar, mas não deveria

# Métodos privados
# Você também pode tornar os métodos privados usando o prefixo de dois sublinhados:
# obs-> os métodos privados não podem ser chamados diretamente de fora da classe. 

class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
calc.add(9)
print(calc.result)
# calc.__validate(5) # Isso causaria um erro, já que o metodo só pode ser acessado dentro da classe por outro metodo
