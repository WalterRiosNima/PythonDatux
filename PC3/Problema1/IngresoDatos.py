""""Ingreso de Datos"""

def get_int(msg: str='Ingrese un número entero: ')->int:
    """Solicita un número entero"""
    try:
        x = int(input(msg))
        return x
    except ValueError:
        print("Error, debe introducir números enteros")
        return get_int(msg)