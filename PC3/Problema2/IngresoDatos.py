"""Contiene Funciones para el ingreso de los datos"""

def get_str_clean(msg:str='Ingrese un texto: ')->str:
    """Permite el ingreso de un dato de tipo texto, limpiando espacios"""
    response = input(msg)
    return response.strip()