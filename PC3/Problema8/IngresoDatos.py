"""Contiene funciones de ingreso de Datos"""
def get_float(num)->float:
    """Solicita un número real"""
    try:
        x = float(input(num))
        return x
    except:
        print("Error, debe ingresar un número")
        return get_float("Inténtelo nuevamente: ")