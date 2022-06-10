"""Funcion que divide los números"""

def dividir(x:float,y:float)->float:
    """Divide dos números"""
    try:
        return x/y
    except ZeroDivisionError:
        print("Entrada no válida")