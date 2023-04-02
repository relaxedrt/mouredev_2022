'''Enunciado: Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
    - El .txt se corresponde con las entradas de una calculadora.
    - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
    - Soporta números enteros y decimales.
    - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
    - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
    - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.'''

f = open("21_CALCULADORA\challenge21.txt")

#Cogemos el primer digito y lo usamos para el resto de aplicaciones
res = f.readline(1)
#guardamos el ultimo simbolo
ls = ""

for linea in f.readlines():
    if ls == "+":
        res += linea
    if ls == "-":
        res -= linea
    if ls == "*":
        res *= linea
    if ls == "/":
        res /= linea
