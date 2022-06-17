import re 
regex = r""

def numLineasFicheroRuta(ruta):
    numLineas = -1
    fichero = open(ruta, 'r')
    numLineas = len(fichero.readlines())
    fichero.close()
    return numLineas


def numLineasVacias(ruta):
    """Encuentra el número de líneas vacias y líneas llenas de espacios"""
    numLineasV=0
    f = open(ruta, 'r')
    lines = f.readlines()
    for line in range(len(lines)):
        if lines[line] == '\n' or  len(lines[line].strip()) == 0 or lines[line] in ['\n', '\r\n']:
            numLineasV=numLineasV+1
    f.close()
    return numLineasV

def numLineasComent(ruta):
    numLineasC=0
    f = open(ruta, 'r')
    lines = f.readlines()

    for line in range(len(lines)):
        re.search('#', lines[line])
        palabra1 = "#"
        encontrado1 = re.search(palabra1, lines[line])
        if re.match(regex, lines[line]) and encontrado1:
            numLineasC=numLineasC+1
    f.close()
    return numLineasC

def numeroLineasCódigo(numLineas, numLineasV, numLineasC):
    return numLineas-numLineasV-numLineasC