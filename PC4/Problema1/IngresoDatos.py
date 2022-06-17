""""Ingreso de Datos"""


def get_int(msg: str='Ingrese un número entero postivo: ')->int:
    """Solicita un número entero"""
    try:
        x = int(input(msg))
        return x
    except ValueError:
        print("Error, debe introducir números enteros")
        return get_int()
    
def intpos(x):
    """Verifica si un número entero es positivo """
    if x>0:
        return x
    else:
        return get_int()
    