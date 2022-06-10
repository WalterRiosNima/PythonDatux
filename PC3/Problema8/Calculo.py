import Operaciones as Op
import IngresoDatos as ID


MSG="""VERIFICAMOS EL FUNCIONAMIENTO DE LAS FUNCIONES
Ejecutando funciones...
"""

def calculo():
    numero1= ID.get_float("Ingrese el primer número: ")
    numero2= ID.get_float("Ingrese el segundo número: ")
    
    print( "\nSuma: {} + {} = {}".format(numero1, numero2, Op.sumar(numero1, numero2) ) )
    print( "Resta: {} - {} = {}".format(numero1, numero2, Op.restar(numero1, numero2) ) )
    print( "Multiplicación: {} x {} = {}".format(numero1, numero2, Op.producto(numero1, numero2) ) ) 
    print( "División: {} ÷ {} = {}".format(numero1, numero2, Op.division(numero1, numero2) )) 


calculo()


