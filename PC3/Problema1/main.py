
import IngresoDatos as ID
import FuncionesBasicas as FB

def main():
    x = ID.get_int("Introduce X: ")
    y = ID.get_int("Introduce Y: ")
    div_=FB.dividir(x, y)
    if x>y:
        print("Intente nuevamente.")
        return main()
    elif 1>=div_>0.99:
        print("F")
    elif 0<=div_<0.01:
        print("E")
    elif div_<0:
        print("Entrada no válida")
        return main()
    else:
        print("{}%".format(round(100*div_)))



if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)