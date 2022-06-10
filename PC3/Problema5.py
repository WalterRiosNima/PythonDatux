import random as rd 

class Alumno:
    def __init__(self, nombre, registro):
        self.registro = registro
        self.nombre = nombre
        
    def Display(self):
        print("(Nombre: {}, Registro: {})".format(self.nombre, self.registro))
    
    
    
    def setAge(self):
        #Se asigna una edad aleatoria
        print("Tiene {} años".format(rd.randint(3, 17)))
        
        #Se asigna una nota aleatoria
    def setNota(self):
        print("Tiene {} años".format(rd.randint(1, 20)))      


Alumno1_=Alumno("Walter", 11)
Alumno1_.Display()
Alumno1_.setAge()
Alumno1_.setNota()