'''Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
    Nota: Esta prueba no se puede resolver con el playground online de Kotlin. Se necesita Android Studio.
    Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
    Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.'''
import cv2

def ratio(url):
    img = cv2.imread(url)
    return (img.shape[0]/img.shape[1])

def isint(n):
    if n - int(n) == 0:
        return True
    else:
        return False
    
def aspectratio(ratio:float):
    for i in range (1,100):
        if isint(ratio*i) == True:
            return f"{ratio * i}:{i}"
        print(i)
    return "ERROR"
        
print(isint(1.33*4))
#print(aspectratio(1.33))
