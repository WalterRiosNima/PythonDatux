import IngresoDatos as ID
import FuncionesLineasCodigo as FLC


def main():
    ruta=ID.get_rute_clean("Ingrese la ruta del archivo:")
    numLineas = FLC.numLineasFicheroRuta(ruta)
    numLineasV = FLC.numLineasVacias(ruta)
    numLineasC = FLC.numLineasComent(ruta)  
    return FLC.numeroLineasCódigo(numLineas, numLineasV, numLineasC)
      
print("\nEl archico tiene {} líneas de código" .format( main()))