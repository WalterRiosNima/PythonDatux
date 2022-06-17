from pyfiglet import Figlet
import IngresoDatos as ID

def main():
    figlet = Figlet()
    texto=ID.get_str_clean("Ingrese un texto: ")
    fuente=ID.get_str_in("Ingrese una fuente: ")
    figlet.setFont(font=fuente)
    MSG=print(figlet.renderText(texto))
    return MSG
    
    
if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)