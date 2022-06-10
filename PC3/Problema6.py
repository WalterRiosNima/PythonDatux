import math

class Punto:
    
    def __init__(self, coordenadaX=0, coordenadaY=0) -> None:

        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY

    def __str__(self):
        return  "({},{})".format(self.coordenadaX, self.coordenadaY)
    
    def cuadrante(self):
        if self.coordenadaX > 0 and self.coordenadaY > 0:
            print("El punto {} pertenece al Primer Cuadrante".format(self))
            
        elif self.coordenadaX > 0 and self.coordenadaY < 0:
            print("El punto {} pertenece al Cuarto Cuadrante".format(self))
            
        elif self.coordenadaX < 0 and self.coordenadaY > 0:
            print("El punto {} pertenece al Segundo Cuadrante".format(self))
            
        elif self.coordenadaX < 0 and self.coordenadaY < 0:
            print("El puntto {} pertenece al Tercer Cuadrante".format(self))
            
        elif self.coordenadaX != 0 and self.coordenadaY == 0:
            print("El punto {} se sitúa sobre el eje X".format(self))
            
        elif self.coordenadaX == 0 and self.coordenadaY!= 0:
            print("El punto {} se sitúa sobre el eje Y".format(self))
            
        else:
            print("El punto {} se encuentra sobre el ORIGEN".format(self))
            
    def vector(self, puntoF):
        "self -> puntoI"
        "Vector IF = (puntoFx-puntoIx ; puntoFy - puntoIy)"
        print("El vector {}{} es ({},{})".format(self, puntoF, puntoF.coordenadaX - self.coordenadaX, puntoF.coordenadaY - self.coordenadaY) )
        
        
        
    def distancia(self, punto2):
        "self -> punto1 "
        "distancia = sqrt(|(punto1x-punto2x)**2- (punto1y-punto2y)**2|)" 
        
        distancia_ = math.sqrt((punto2.coordenadaX - self.coordenadaX)**2 + (punto2.coordenadaY - self.coordenadaY)**2)
        print("La distancia entre {} y {} es {}".format(self, punto2, round(distancia_,2)))
        
class Rectangulo:
    
    def __init__(self, puntoI=Punto(), puntoF=Punto()):
        self.puntoI = puntoI
        self.puntoF = puntoF
   
        
    def base(self):
        "base = |puntoIx-puntoFx|"
        self.base_ = abs(self.puntoF.coordenadaX - self.puntoI.coordenadaX)
        print("La Base del rectángulo formado por {} y {} es: {}".format(self.puntoI,self.puntoF,self.base_))
        
        
    def altura(self):
        "base = |puntoIy-puntoFy|"
        self.altura_ = abs(self.puntoF.coordenadaY - self.puntoI.coordenadaY)
        print("La Altura del rectángulo formado por {} y {} es: {}".format(self.puntoI, self.puntoF,self.altura_))
        
    def area(self):
        "área = base*altura"
        self.area_ = self.base_ * self.altura_
        print("El Área del rectángulo formado por {} y {} es: {}".format(self.puntoI,self.puntoF,round(self.area_,2)))

    


     
# EXPERIMENTACIÓN       
#Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla. 
A = Punto(2,2)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)
  


print("\nVERIFICACIÓN\n\nCuadrante")  
# Consulta a que cuadrante pertenecen el punto A, C y D.
A.cuadrante()
C.cuadrante()
D.cuadrante()

# Consulta los vectores AB y BA.
print("\nVectores")
A.vector(B)
B.vector(A)

# (Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
print("\nDistancias")
A.distancia(B)
B.distancia(A)

# (Optativo) Determina cual de los 3 puntos A, B o C, 
# se encuentra más lejos del origen, punto (0,0).
# Origen=D
print("\nDistanacias el origen")
A.distancia(D)
B.distancia(D)
C.distancia(D)

#Crea un rectángulo utilizando los puntos A y B.
R = Rectangulo(A,B)

#Consulta la base, altura y área del rectángulo.
print("\nRectángulo")
R.base()
R.altura()
R.area()