'''Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
    Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
    NO se tienen en cuenta los espacios, signos de puntuación y tildes.
    Ejemplo: Ana lleva al oso la avellana.'''
def isPalindrome(x):
        p1 = []
        p2 = []
        for i in x:
            if i != " ":
                p1.append(i)
                p2.append(i)
        p1.reverse()
        if p1 == p2:
            return True
        else:
            return False 
print(isPalindrome("ana lleva al oso la avellana"))
print(isPalindrome("212"))