'''Enunciado: Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno). ¿De cuántas maneras eres capaz de hacerlo? Crea el código para cada una de ellas.'''

#Con un for
def confor():
    for i in range(1,101):
        print(i)
#confor()

#Con un while
def conwhile():
    i = 1
    while i != 101:
        print(i)
        i += 1
#conwhile()