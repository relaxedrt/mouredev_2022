'''Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
    poner en mayúscula la primera letra de cada palabra.'''
def mayusculador(frase : str):
    frase_low = (frase.lower()).split(" ")
    res = []
    for i in frase_low:
        res.append(i.capitalize())
    print(" ".join(res))

    

mayusculador("cacota de perro")