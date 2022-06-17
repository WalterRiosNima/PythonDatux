"""funciones para Ingresar datos"""

def get_float(msg: str='Ingrese un número decimales: ')->float:
    """Solicita un número entero"""
    try:
        x = float(input(msg))
        return x
    except ValueError:
        print("Error, debe introducir números decimales")
        return get_float(msg)