#%% PC2

#%% PROBLEMA 1

print("Los números son: ")
for i in range (1500,2701):
    if i%7==0 and i%5==0:
        print (i)


#%% PROBLEMA 2

for j in range (5):
    print("* "*(j))
for k in range (5):
    print("* "*(5-k))
    
    
#%% PROBLEMA 3

numeros=[]
pares_numeros=[]
impares_numeros=[]
while True:
    opcion=input("Quiere ingresar un número?: ")
    if opcion.lower() =='si':
        numero=int(input("Ingrese el número: "))
        numeros.append(numero)
    elif opcion.lower() == 'no':
        break
    else:
        print("Entrada inválida, intente nuevamente.")
for l in range(len(numeros)):
    if numeros[l]%2==0:
        pares_numeros.append(numeros[l])
    else:
        impares_numeros.append(numeros[l])
        
print("Los números ingresados son:\n",numeros)
print("Cantidad de números pares: ",len(pares_numeros))
print("Cantidad de números impares: ",len(impares_numeros))


#%% PROBLEMA 4

lista_sistema=[]
n = int(input("Ingrese el número de alumnos:"))
for m in range(n):
    sistema = {}
    notas=[]
    nombre=input("Ingrese el nombre del alumno {}:  ".format(m+1))
    for o in range(3):
        nota = float(input("Ingrese la nota {}: ".format(o+1)))
        notas.append(nota)
    sistema[nombre] = notas
    lista_sistema.append(sistema)
print("Los alumnos y sus notas son: ")
for p in lista_sistema:
    print(p)
    
    
#%% PROBLEMA 5

def contarnumero(numero,digito):
    numero2=[]
    numero2=list(map(int, str(numero)))
    return numero2.count(digito)

numero = int(input("Ingrese el número:"))
digito = int(input("Ingrese el dígito:"))
print("Cantidad de veces {} en el número {}: {}".format(digito,numero,contarnumero(numero,digito)))


#%% PROBLEMA 6

def fibonacci():
    fibo = [0, 1,1]
    for r in range(2,49):
        fibo[r] = fibo[r-1] + fibo[r-2]
        fibo.append(fibo[r])
    return fibo

print(fibonacci())


#%% PROBLEMA 7

def primo(num):
    if num<2:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
        else:
            return True
numero_=int(input("Ingrese un número para saber si es primo: "))        
primo(numero_)


#%% PROBLEMA 8

def factorial(num1):
    fact=1
    if num1==0 or num1==1:
        return 1
    elif num1 > 1:
        for dd in range (1,num1+1):
            fact=fact*dd
        return fact
    else:
        print("Ingrese una opción válida")
    
num1=int(input("Ingrese un número: "))
print("El factorial de {} es: {}" .format(num1,factorial(num1)))


#%% PROBLEMA 9

texto = input("Ingrese una frase o texto: ")
texto2=''
for kk in texto:
    if kk.lower()=='a' or kk.lower()=="e" or kk.lower()=="i" or kk.lower()=="o" or kk.lower()=="u" : 
        texto2 += ''
        continue
    texto2 += kk
print(texto2)


#%% PROBLEMA 10

while True:
    fecha=input("Ingrese una fecha: ")

    fecha2=''
    for k in fecha:
        if  k=="," or k==" " or k=="/" or k=="-" or k==".": 
            fecha2 += '.'
            continue
        fecha2 += k
    fecha2=fecha2.split(".")

    posicion=0
    while posicion<len(fecha2):
        if fecha2[posicion]=="":
            fecha2.pop(posicion)
        else:
            posicion=posicion+1
    if len(fecha2)==3:
        break
    else:
        print("Entrada inválida, intente nuevamente,")
        
meses=[]        
meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

mes=fecha2[0].lower()
dia=fecha2[1]
anio=fecha2[2]
    
if fecha2[0].isnumeric()==True:
    mes=fecha2[0]    
else:
    for qq in range(len(meses)):
        if mes==meses[qq]:
            mes=qq+1

print("{}-{}-{}".format( anio, str(mes).zfill(2),str(dia).zfill(2)))


#%% PROBLEMAS ADICIONALES

#%% PROBLEMA 1 - MARIO GAME - Mario.py

while True:
    altura=input("Ingrese la altura de la media pirámide: ")
    if altura.isnumeric()==True:
        altura=int(altura)
        if 1<=altura<=8:
            for j in range (altura):
                print("  "*(altura-j)+"# "*(j+1))
            break
        else:
            print("El número no está entre 1 y 8. Entrada inválida, intente nuevamente.")
    else:
        print("Entrada inválida, intente nuevamente.")
        

#%% PROBLEMA 2 - SUBSTITUCION - substitucion.py

import string

abecedario = list(string.ascii_lowercase)
ciphertext=[]
while True:
    llave_sustitucion=input("Ingrese la llave de sustitucion: ")
    if len(llave_sustitucion)==len(abecedario) and set(llave_sustitucion.lower())==set(abecedario):
        plaintext=input("Ingrese el texto plano: ")
        llave_sustitucion=list(llave_sustitucion)
        plaintext=list(plaintext)

        for xx in range(len(plaintext)):
            for ll in range(len(abecedario)):
                if plaintext[xx].islower()==True:
                    if plaintext[xx]==abecedario[ll]:
                        ciphertext.append(llave_sustitucion[ll].lower())
                else:
                    if plaintext[xx]==abecedario[ll]:
                        ciphertext.append(llave_sustitucion[ll])
            if plaintext[xx] not in abecedario: 
                    ciphertext.append(plaintext[xx])
        break
    else:
        print("Error")

ciphertext="".join(ciphertext)
print(ciphertext)


#%% PROBLEMAS DIVERSOS

# Nota: Estos ejercicios se realizaron de manera correlativa, es decir
# usando las listas, variables y diccionarios de items del mismo.

#%% 1.

carga_alumnos=[]
nombres=[]
nn = int(input("Ingrese el número (n) de alumnos:"))

for mm in range(nn):
    carga = {}
    notas_alum=[]
    
    nombre_alum=input("Ingrese el nombre del alumno {}: ".format(mm+1))
    nombres.append(nombre_alum)
    for op in range(3):
        while True:
            nota_alum = float(input("Ingrese la nota {}: ".format(op+1)))
            if 0<=nota_alum<=10:
                break
            else:
                print("Las notas deben estar comprendidas entre 0 y 10.")
        notas_alum.append(nota_alum)
        
    
    carga[nombre_alum] = notas_alum
    carga_alumnos.append(carga)
    
print("Los alumnos y sus notas son: ")
for p in carga_alumnos:
    print(p)   


#%% 2.

aprobados=0
desaprobados=0
promedios=[]
for ii in range(len(carga_alumnos)):
    suma=0
    print(carga_alumnos[ii])
    for yy in range(3):
        suma+=carga_alumnos[ii][nombres[ii]][yy]
    promedio=suma/3
    promedios.append(promedio)
    if promedio>=4:
        print("Aprobado, con promedio ", promedio)
        aprobados+=1
    else:
        print("Desaprobado, con promedio ", promedio)
        desaprobados+=1
print("\nNúmero de aprobados: ", aprobados)
print("Número de desaprobados: ", desaprobados)


#%% 3.
#El promedio de las tres notas de los alumnos se realizó en el item anterior.

suma_aula=0
promedio_aula=0
for ii in range(len(carga_alumnos)):
    suma=0
    print(carga_alumnos[ii])
    for yy in range(3):
        suma+=carga_alumnos[ii][nombres[ii]][yy]
    promedio=suma/3
    suma_aula+=promedio
promedio_aula=suma_aula/nn
print("Promedio del aula: ", promedio_aula)


#%% 4.

maximo_promedio=max(promedios)
minimo_promedio=min(promedios)
posi_max=promedios.index(max(promedios))
posi_min=promedios.index(min(promedios))
print("El promedio mas alto es el de {} con {}" .format(nombres[posi_max], maximo_promedio))
print("El promedio mas bajo es el de {} con {}" .format(nombres[posi_min], minimo_promedio))

