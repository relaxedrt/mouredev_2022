'''Enunciado: Crea un programa se encargue de transformar un número decimal a binario 
    sin utilizar funciones propias del lenguaje que lo hagan directamente.'''
def dectobin(dec):
    res = []
    while dec / 2 != 1:
        print(dec)
        if dec % 2 == 1:
            res.append(1)
        if dec % 2 == 0:
            res.append(0)
        dec /= 2
    if dec / 2 == 1:
        res.append(1)
    return res.reverse()

print(dectobin(8))