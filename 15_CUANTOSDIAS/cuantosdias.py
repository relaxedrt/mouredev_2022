'''Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
    Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
    La función recibirá dos String y retornará un Int.
    La diferencia en días será absoluta (no importa el orden de las fechas).
    Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.'''
import datetime
def dateconversor(f1 : str):
    #introduzco una gestión básica de errores y un pokayoke de variables
    try:
        #separamos las cifras de la fecha
        f11 = f1.split("/")
        f111 = []
        #la invertimos
        for i in range(len(f11)-1,-1,-1):
            f111.append(int(f11[i]))
        #la convertimos en tipo fecha
        return datetime.datetime(f111[0], f111[1], f111[2])
    except:
        print("Ha habido un error en la conversión, la fecha no esta bien especificada.")
        exit()

def diferenciafechas(d1 : datetime, d2 :datetime):
    return d1 - d2
print(diferenciafechas(dateconversor("20/11/2001"), dateconversor("20/11/1")))
#print(dateconversor("20/11/2001"))