'''Enunciado: Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros.
    - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.'''

def maxcomdiv(num1, num2):
    temp = 0
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1

def mincommul(num1, num2):
    return (num1 * num2) / maxcomdiv(num1, num2)

print(maxcomdiv(10, 15))
print(mincommul(10, 15))