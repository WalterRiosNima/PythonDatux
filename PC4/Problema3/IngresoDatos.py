from pyfiglet import Figlet
import random

def get_str_clean(msg:str='Ingrese un texto: ')->str:
    """Permite el ingreso de un dato de tipo texto, limpiando espacios"""
    response = input(msg)
    return response.strip()

def get_str_in(msg:str='Ingrese un texto: ')->str:
    """Permite el ingreso de un dato de tipo texto, limpiando espacios y verificando si es
    una fuente aceptable"""
    response = input(msg)
    figlet = Figlet()
    if response.strip() in figlet.getFonts():
        return response
    else:
        print("No es una fuente válida, se escogerá una aleatoriamente...")
        return random.choice(figlet.getFonts())