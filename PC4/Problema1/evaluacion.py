"""Encuentra a un número introducciendo tests por el teclado"""

def evalua(numero):
    try:
        num = int(input("Guess: "))
        if numero == num:
            print("¡Adivinaste! ")
        elif numero > num:
            print("¡Demasiado pequeño!")
            return evalua(numero)
        elif numero < num:
            print("¡Te pasaste!")
            return evalua(numero)
        else:
            print("Comando no válido")
            return evalua(numero)
    except:
        print("Comando no válido")
        return evalua(numero)