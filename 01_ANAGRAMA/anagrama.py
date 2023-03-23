'''Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
    Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
    NO hace falta comprobar que ambas palabras existan.
    Dos palabras exactamente iguales no son anagrama.'''
def anagrama(str1, str2):
    if str1 == str2:
        return False
    if list(str1) in list(str2):
        return True
print(anagrama(input(f"Primera palabra: "),input(f"Segunda palabra: ")))
