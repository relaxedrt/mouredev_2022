'''Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
    Hecho esto, imprime los números primos entre 1 y 100.'''
def primo(num):
    for x in range(2,11):
        if num != x:
            if num % x == 0:
                return True
            
for i in range(0,101):
    if primo(i) == True:
        print(f"{i} no es primo.   ")
    else:
        print(f"{i} es primo.")
