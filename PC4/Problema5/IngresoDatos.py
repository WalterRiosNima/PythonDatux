""""Ingreso de la ruta de un fichero"""


def get_rute_clean(msg:str='Ingrese una ruta: ')->str:
    """Permite el ingreso de un dato de tipo texto, o se limpiar los espacios"""
    ruta = input(msg).strip()
    try:
        fichero = open(ruta, 'r')
        fichero.close()
    except AttributeError:
        print("Debes insertar un fichero")
        return get_rute_clean()
    except FileNotFoundError:
        print("la ruta no es correcta")
        return get_rute_clean()
    return ruta.strip()
    