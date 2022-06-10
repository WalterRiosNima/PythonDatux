import math

class Circulo():
    
    def __init__(self, radio):
        self.radio = radio
       
        
    def areaC(self):
        
        self.areaC_=math.pi*self.radio**2
        print("El área del cicrulo de radio {} es: {}". format(self.radio, round(self.areaC_,2)))


C1 = Circulo(3)
C1.areaC()