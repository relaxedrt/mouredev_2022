'''Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
'''
def factorial0toX(x):
    res = 1
    #recorremos todos los numeros desde el 1 al numero dado.
    for i in range(1,x):
        #recorremos todos los numeros desde el 1 al que estamos
        for j in range(1, i+1):
            #multiplicamos los numeros recorridos
            res *= j
        print(f"Factorial de {i} = {res}")
        #reseteamos la variable
        res = 1    
factorial0toX(10)
