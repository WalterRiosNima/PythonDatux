import numeroaleatorio as NA
import evaluacion as EV
import IngresoDatos as ID


def main():
    level = ID.intpos(ID.get_int("Ingrese el level: "))
    n = NA.numero_aleatorio(level)
    return EV.evalua(n)

if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)