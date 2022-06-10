"""Contiene operaciones básica y sus excepsiones"""

def sumar(num1:float,num2:float)->float:
    """Calcula y verifica la suma de dos números"""
    try:
        suma_ = num1+num2
    except TypeError:
        print("Error: Tipo de dato no válido")
        return "No se puede."
    else:
        return suma_


def restar(num1:float,num2:float)->float:
    """Calcula y verifica la resta dos números"""
    try:
        resta_ =  num1-num2
    except TypeError:
        print("Error: Tipo de dato no válido")
        return "No se puede"
    else:
        return resta_


def producto(num1:float,num2:float)->float:
    """Calcula y verifica el producto de dos números"""
    try:
        #Esta línea de código verifica si num1*num2 resulta un número, ya que
        #una cadena por un entero hace que la cadena se repita y escapa del
        # TypeError
        abs(num1*num2)
    except TypeError:
        print("Error: Tipo de dato no válido")
        return "No se puede"
    else:
        return num1*num2


def division(num1:float,num2:float)-> float:
    """Calcula y verifica el cociente entre dos números"""
    try:
        divide_ = num1/num2
    except TypeError:
        print("Error: Tipo de dato no válido")
        return "No se puede"
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")
        return "No se puede"
    else:
        return divide_