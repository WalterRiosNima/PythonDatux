"""Funciones"""

def notasCadena(notas):
    "Convierte en una lista una cadena con separaciones por comas"
    notas2=''
    notas2=notas.split(",")
    return notas2

def barrerEnteroLista(lista):
    """Verifica si todos los elementos de una cadena son enteros"""
    for tt in range(len(lista)):
        try:    
            int(lista[tt])
            mensaje="Correcto"
        except ValueError:
            mensaje="Error de formato"
            break
    return mensaje