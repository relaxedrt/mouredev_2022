'''Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
    Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
    NO hace falta comprobar que ambas palabras existan.
    Dos palabras exactamente iguales no son anagrama.'''

def ana(w1 : str, w2: str):
    #convertimos la palabra a minusculas
    w1 = w1.lower()
    w2 = w2.lower()
    #convertimos cada palabra en una lista
    l1 = list(w1)
    l2 = list(w2)
    #ordenamos las listas
    l1.sort()
    l2.sort()
    #convertimos de vuelta a palabra
    w1o = str(l1)
    w2o = str(l2)
    #comprobamos si son iguales 
    return w1o == w2o

print(ana(input(f"Primera palabra: "),input(f"Segunda palabra: ")))

