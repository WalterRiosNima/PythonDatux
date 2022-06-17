import ingresoDatos as ID
import opciones as op

def main():
    print("Problema 4:")
    while True:
        opcion=ID.int1to4(ID.get_int("""MENÚ
1. Guardar fichero
2. Leer fichero
3. Leear una línea de un fichero
4. Salir                             
Ingreso una opción: """))
        if opcion==1:
            n=ID.int1to10(ID.get_int("Ingrese un valor entre 1 y 10: "))
            op.opcion1(n)
        
        elif opcion==2:
            n=ID.int1to10(ID.get_int("Ingrese un valor entre 1 y 10: "))
            op.opcion2(n)
            
        elif opcion==3:
            n=ID.int1to10(ID.get_int("Ingrese un valor entre 1 y 10: "))
            m=ID.int1to10(ID.get_int("Ingrese otro valor entre 1 y 10: "))
            op.opcion3(n, m)
        elif opcion==4:
            break

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)


    