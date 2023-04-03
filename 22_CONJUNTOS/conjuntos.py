'''Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
    - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
    - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
    - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.'''

def conjuntos(arr1 : list, arr2 : list, conj : bool):
    res = []
    if conj == True:
        for i in arr1:
            if i in arr2:
                res.append(i)
    if conj == False:
        for i in arr1:
            if i not in arr2:
                res.append(i)
        for j in arr2:
            if j not in arr1:
                res.append(j)
    return(res)

print(conjuntos([1,2,3], [3,4,5], True))
print(conjuntos([1,2,3], [3,4,5], False))