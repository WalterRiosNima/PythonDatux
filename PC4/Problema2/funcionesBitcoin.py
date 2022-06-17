"""Funciones empleadas para tratar con Bitcoins"""

import requests
import locale

def get_url_data(url):
    """Condigue data de un url en formato .json"""
    try:
        response=requests.get(url)
    except requests.RequestException:
        return get_url_data()
    else: 
        data=response.json()
    return data



def get_str_to_number(texto):
    """Convierte un numero de tipo string con comas y puntos decimales a un número de tipo
    flotante, cambiando el formato de este"""
    locale.setlocale(locale.LC_ALL, '')
    return locale.atof(texto)


def conv_Bitcoin_to_USD(n, bitcoin_priceusd):
    return n*bitcoin_priceusd