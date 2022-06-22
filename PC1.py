#%% PC1
#%% Problema 1:

nombre = input("Ingrese su nombre: ")
print("¡Hola %s!" %(nombre))



#%% Problema 2:
    
consumo=float(input("¿Cuánto fue su consumo? Ingrese su consumo: "))
porcentajePropina=float(input("¿Cuanto de propina en porcentaje (%) quiere dar como propina?\nIngrese el porcentaje: "))
propina=consumo*porcentajePropina/100
print("Su propina será: %.2f" %(propina))



#%% Problema 3:
    
payasos=int(input("Ingrese el número de payasos: "))
muñecas=int(input("Ingrese el número de muñecas: "))
pesoPaquete=payasos*112+muñecas*75
print("El peso total del paquete es de %i gramos" %(pesoPaquete))



#%% Problema 4:
    
N=int(input("Ingrese el valor de N: "))
sumaN=N*(N+1)/2
print("El valor de la suma de todos los enteros desde 1 hasta %i es: %i " %(N,sumaN))



#%% Problema 5:
    
shows=int(input("Ingrese el número de shows: "))
if shows>3:
    k=True
else:
    k=False
print(k)



#%% Problema 6:
    
edad=int(input("Ingrese su edad: "))
precio=0
if edad>=18:
    precio=10
    print("El costo es de : %i" %(precio))
elif edad>=4:
    precio=5
    print("El costo es de : %i" %(precio))
else:
    print("Ingresa gratis")



#%% Problema 7:
    
numero1=float(input("Ingrese el primer número: "))
numero2=float(input("Ingrese el segundo número: "))

opcion=int(input("""\nOPCIONES:\n
1.Mostrar la suma de los dos números.
2.Mostrar una resta de los dos números (el primero menos el segundo).
3.Mostrar una multiplicación de los dos números.
\nIngrese la opción: """))

if opcion==1:
    print("La suma es: ",numero1+numero2)
elif opcion==2:
    print("La resta es: ",numero1-numero2)
elif opcion==3:
    print("La multiplicaión es: ", numero1*numero2)
else:
    print("Ingrese una opción válida,")



#%% Problema 8:
    
hora=input("Ingrese la hora: ")
verificarhora=hora.split(":")
if len(verificarhora)==2:
    horas, minutos = hora.split(":")
    horas=int(horas)
    minutos=int(minutos)
    if horas>=18 and horas<19:
        print("Es hora de cenar")
    elif horas==19 and minutos==00:
        print("Es hora de cenar")
    elif horas>=7 and horas<8:
        print("Es hora de desayunar")
    elif horas==8 and minutos==00:
        print("Es hora de desayunar")        
    elif horas>=12 and horas<13:
        print("Es hora de almorzar")
    elif horas==13 and minutos==00:
        print("Es hora de almorzar")
    else:
        print("")
else:
    print("Ingrese una hora válida.")



#%% Problema 9:
    
lista1 =['Di', 'buen', 'día', 'a', 'papa']
lista2=lista1.copy()
lista2.reverse()
print(lista1)
print(lista2)



#%% Problema 10:
    
listamuestra=['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
listainicial=listamuestra.copy()
posiciones= [0,4,5]
posiciones.reverse()

for i in range(len(posiciones)):
    listamuestra.remove(listamuestra[posiciones[i]])
print(listainicial)
print(listamuestra)



#%% Problema 11:
    
listaOriginal=[1, 1, 2, 3, 4, 4, 5, 1]
listaProcesada=[]

for j in listaOriginal:
    if j not in listaProcesada:
        listaProcesada.append(j)
print(listaOriginal)
print(listaProcesada)



#%% Problema 12:

archivo=input("Ingrese el nombre del archivo: ")
x=archivo.split(".")
if len(x)==2:
    nombreArchivo, extension = archivo.split(".")
    extension=extension.lower()
    
    amime={"gif":"image/gif","jpg":"image/jpeg","jpeg":"image/jpeg",
           "png":"image/png","pdf":"application/pdf","txt":"text/plain",
           "zip":"application/zip"}
    
    if extension in amime:
       print(amime[extension])
    else :
        print("application/octet-stream")
else:
    print("Ingrese un nombre de archivo válido.")
   
    
    
    
#%% EJERCICIOS ADICIONALES - Ejercicios diversos
#%% EJERCICIO 1.

C=float(input("Ingrese el monto a depositar: "))
r=4
t=3

for m in range(t):
    Cf=C*(1+r/100)**(m+1)
    print("Ahorros tras el año %i es de %.2f" %(m+1,Cf))
 
    
 
#%%  EJERCICIO 2.

from math import sqrt
print("Ingrese los coeficientes de la ecuación de segundo grado (a x² + b x + c = 0)")
a=float(input("\nIngrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))
c=float(input("Ingrese el valor de c: "))

determinante=b*b-4*a*c
if determinante>0:
    x1=(-b+sqrt(determinante))/(2*a)
    x2=(-b-sqrt(determinante))/(2*a)
    print("\nTiene dos soluciones reales, %.2f y %.2f" %(x1,x2))
elif determinante ==0:
    x1=-b/(2*a)
    print("\nTiene solución unica %.2f" %(x1))
else:
    print("\nEcuación no presenta solución real")
    
