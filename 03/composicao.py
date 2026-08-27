'''
Composição é quando uma classe cria e usa objetos de outras classes como seus atributos, 
formando uma relação do tipo "tem-um" (por exemplo, um carro tem um motor). 
Em vez de herdar características de outra classe inteira, você junta partes menores para construir algo maior.

Reutilização: Você aproveita códigos prontos sem precisar criar uma hierarquia complexa de herança.

Flexibilidade: É fácil trocar uma parte inteira do objeto por outra se o padrão de funcionamento for o mesmo.
'''

class Motor:
    def ligar(self):
        return "Vrum vrum!"

class Carro:
    def __init__(self):
        self.motor = Motor() # Composição
        
    def ligar_carro(self):
        return self.motor.ligar()

x = Carro()
print(x.ligar_carro())