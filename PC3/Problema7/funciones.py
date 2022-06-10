""""Contiene las funciones del problema"""

import random as rd

def listaAleatorios(n):    
    lista = [0]  * n
    for i in range(n):
        lista[i] = rd.randint(1, 100)
    return lista
  

def mostrarLista(lista):
    print(lista)

def ordenarLista(lista):
    lista.sort()
    return mostrarLista(lista)
