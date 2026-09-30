# Exemplo de implementação de classe abstrata
from abc import abstractmethod


class FormaGeometrica:

    @abstractmethod
    def calcular_area(self):
        pass

# Exemplo de implementação de classes concretas.
# Foram criados dois métodos para cada classe que representa uma Figura Geométrica.
# O método __init__ responsável por construir os objetos da classe.
# O método calcular_area responsável por efetuar o cálculo da área conforme a Figura Geométrica, porém, utiliza
# o mesmo método definido na classe abstrata com suas devidas particularidades.
# O cálculo da área será refeito para cada figura, segundo seu comportamento.
import math

class Retangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def calcular_area(self):
        figura = ['Retângulo']
        figura.append(self.base * self.altura)
        return figura

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    def calcular_area(self):
        figura = ['Círculo']
        figura.append(self.raio * self.raio * math.pi)
        return figura

class Quadrado(FormaGeometrica):
    def __init__(self, base):
        self.base = base
    def calcular_area(self):
        figura = ['Quadrado']
        figura.append(self.base * self.base)
        return figura

# Exemplo do uso do Polimorfismo.
# A variável retangulo1 representa um retângulo de base 4cm e altura 8cm.
# A variável retangulo2 representa um retângulo de base 6cm e altura 10cm.
# A variável quadrado1 representa um quadrado com 4cm de lado.
# A variável quadrado2 representa um quadrado com 6cm de lado.
# A variável circulo1 representa um círculo de 4cm de raio.
# A variável circulo2 representa um círculo de 6cm de raio.
# A variável formas_geometricas armazena uma lista de figuras.

retangulo1 = Retangulo(4, 8)
retangulo2 = Retangulo(6, 10)
quadrado1 = Quadrado(4)
quadrado2 = Quadrado(6)
circulo1 = Circulo(4)
circulo2 = Circulo(6)

formas_geometricas = [retangulo1, retangulo2, quadrado1, quadrado2, circulo1, circulo2]

area = 0
for i, forma in enumerate(formas_geometricas):
    area = forma.calcular_area()
    print(f"A área da figura {i+1} – {area[0]} foi de {round(area[1], 2)} m2.")