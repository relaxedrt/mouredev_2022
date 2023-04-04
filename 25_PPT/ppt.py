'''Enunciado: Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
    - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
    - La función recibe un listado que contiene pares, representando cada jugada.
    - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
    - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".'''

def ppt(partida: list):
    res = ""
    p1 = partida[0]
    p2 = partida[1]
    if p1 == "R":
        if p2 == "R":
            res = "Tie"
        if p2 == "P":
            res = "Player 2"
        if p2 == "S":
            res = "Player 1"
    if p1 == "P":
        if p2 == "R":
            res = "Player 1"
        if p2 == "P":
            res = "Tie"
        if p2 == "S":
            res = "Player 2"
    if p1 == "S":
        if p2 == "R":
            res = "Player 2"
        if p2 == "P":
            res = "Player 1"
        if p2 == "S":
            res = "Tie"
    return res

def statistics(partidas):
    p1 = 0
    p2 = 0
    tie = 0
    for partida in partidas:
        res = ppt(partida)
        if res == "Player 1":
            p1 += 1
        if res == "Player 2":
            p2 += 1
        if res == "Tie":
            tie += 1
    if (p1 > p2) and (p1 > tie):
        return "Player 1"
    if (p2 > p1) and (p2 > tie):
        return "Player 2"
    if (tie > p2) and (tie > p1):
        return "Tie"

print(statistics([("R","S"), ("S","R"), ("P","S")]))