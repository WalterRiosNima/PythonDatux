
import IngresoDatos as ID
import Funciones as F

def main():
    lista=ID.get_str_clean("Ingrese la lista de calificaciones, separadas unicamente por comas: ")
    print(F.barrerEnteroLista(F.notasCadena(lista)))

main()

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)