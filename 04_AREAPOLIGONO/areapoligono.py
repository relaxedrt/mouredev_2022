'''Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
    La función recibirá por parámetro sólo UN polígono a la vez.
    Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
    Imprime el cálculo del área de un polígono de cada tipo.'''

def areapol(pol, base, altura):
    match pol:
        case "triangulo":
            return ((base * altura)/2)
        case "cuadrado":
            return base * altura
        case "rectangulo":
            return base * altura
        case _:
            return "Error"
    
