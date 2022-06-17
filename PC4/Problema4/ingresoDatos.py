""""Ingreso de Datos"""


def get_int(msg: str='Ingrese un número entero postivo: ')->int:
    """Solicita un número entero"""
    try:
        x = int(input(msg))
        return x
    except ValueError:
        print("Error, debe introducir números enteros: ")
        return get_int()
    
def int1to10(x):
    """Verifica si un número entero está entre 1 y 10: """
    if 1<=x<=10:
        return x
    else:
        return get_int("Ingrese un entero entre 1 y 10: ")
    
def int1to4(x):
    """Verifica si un número entero está entre 1 y 4 """
    if 1<=x<=4:
        return x
    else:
        return get_int("Ingrese un entero entre 1 y 4: ")
    