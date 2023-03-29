'''Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
    out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
    out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.'''
def stripper(str1):
    letras = []
    for i in str1:
        for j in i:
            letras.append(j)
    return letras

def deleter(l1, l2):
    out1 = []
    out2 = []
    for i in l1:
        if i != " ":
            if i not in l2:
                out1.append(i)
    for j in l2:
        if j != " ":
            if j not in l1:
                out2.append(j)
    return "".join(out1), "".join(out2)


print(deleter(stripper("me estaba muriendo"), "podria cagar"))