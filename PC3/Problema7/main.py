import funciones as f

def main():
    n=20
    lista=f.listaAleatorios(n)
    f.mostrarLista(lista)
    f.ordenarLista(lista)
    
    
if __name__=='__main__':
    try:
        main()
    except Exception as e:
        print(e)