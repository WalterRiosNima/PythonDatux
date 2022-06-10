class Rectangulo:
    def __init__(self, largo, ancho):
        
        self.largo = largo
        self.ancho = ancho
        
        
    def area(self):
        self.area_= self.largo * self.ancho
        print("El area del rectángulo es de largo {} y ancho {} es: {}" . format(self.largo, self.ancho, self.area_))

        
R1=Rectangulo(5, 2)

R1.area()