'''Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.'''
sample = {"dia" : 20, "hora" : 20, "minuto" : 20, "segundo" : 20}
def converter(time : dict):
    res = 0
    for i in time:
        if i == "dia":
            res += time[i] * 86400000
        if i == "hora":
            res += time[i] * 3600000
        if i == "minuto":
            res += time[i] * 60000
        if i == "segundo":
            res += time[i] * 1000
    return res    
print(converter(sample))
