'''Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
    Los signos de puntuación no forman parte de la palabra.
    Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
    No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.'''

def word_divider(frase):
    #ponemos la frase en minusculas
    frasemin = frase.lower()
    #quitamos las comas
    commas = frasemin.replace(",", "")
    #quitamos los puntos
    dots = commas.replace(".", "")
    #quitamos los parentesis
    parents = dots.replace("(" or ")", "")
    #separamos por los espacios
    words = parents.split(" ")
    return words

def word_counter(words):
    res = {}
    for word in words:
        num = words.count(word)
        res[word] = num
    return res

print(word_counter(word_divider("Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev).")))
