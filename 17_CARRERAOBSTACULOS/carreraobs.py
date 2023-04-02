'''Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
    carrera de obstáculos.
    - La función recibirá dos parámetros:
        - Un array que sólo puede contener String con las palabras "run" o "jump"
        - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
    - La función imprimirá cómo ha finalizado la carrera:
        - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
            variará el símbolo de esa parte de la pista.
        - Si hace "jump" en "_" (suelo), se variará la pista por "x".
        - Si hace "run" en "|" (valla), se variará la pista por "/".
    - La función retornará un Boolean que indique si ha superado la carrera.
    Para ello tiene que realizar la opción correcta en cada tramo de la pista.'''

def carrera(atleta : list, pista : list):
    #recorremos el array de acciones del atleta
    res = []
    for i in range(0, len(atleta)):
        if atleta[i] == "run":
            if pista[i] == "_":
                res.append("_")
            if pista[i] == "|":
                res.append("x")
        if atleta[i] == "jump":
            if pista[i] == "|":
                res.append("|")
            if pista[i] == "_":
                res.append("x")
    print(res)
    if "x" in res:
        return False
    else:
        return True
    
print(carrera(["run","jump","run","run","run","jump"],["_","|","_","_","_","|"]))
print(carrera(["run","jump","run","run","run","jump"],["_","|","|","_","_","|"]))
        
