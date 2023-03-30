'''Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).
    Si no conoces qué es un número de Armstrong, debes buscar información al respecto.'''
def isamstrong(num : int):
    #convertimos en string para usar cada numero en concreto
    x = str(num)
    res = 0
    #creamos un bucle usando cada numero
    for i in x:
        #cada numero lo elevamos a la cantidad de numeros que tiene el principal
        res += pow(int(i), len(x))
    print(res)
    #si se cumple que sea amstrong devolvemos true
    if res == num:
        return True
    else:
        return False

print(isamstrong(371))
print(isamstrong(23))
    


