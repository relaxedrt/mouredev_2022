'''Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
    Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
    En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
    El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.'''
abctomor = {"a" : ".-", "b" : "-...", "c" : "-.-.", "d" : "-..", "e" : ".", "f" : "..-.", "g" : "--.", "h" : "....", "i" : "..", "j" : ".---",
       "k" : "-.-", "l" : ".-..", "m" : "--", "n" : "-.", "o" : "---", "p" : ".--.", "q" : "--.-", "r" : "-.-", "s" : "...", "t" : "-", "u" : "..-",
       "v" : "...-", "w" : ".--", "x" : "-..-", "y" : "-.--", "z" : "--..", "1" : ".----", "2" : "..---", "3" : "...--", "4" : "....-",
       "5" : ".....", "6" : "-....", "7" : "--...", "8" : "---..", "9" : "----.", "0" : "-----",}
mortoabc = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j',
            '-.-': 'r', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '...': 's', '-': 't', '..-': 'u',
            '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
            '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'}
def detection(string):
    #si alguna letra del abecedario se encuentra en el mensaje sera human readable, sino morse
    for i in abctomor:
        if i in string:
            #devolvemos true si es human readable
            return string, True
    #devolvemos false si recorremos todo el abecedario y ninguna letra matchea y devolvemos a false porque es morse
    return string, False

def traduction(detect):
    string = detect[0].split(" ")
    print(string)
    idiom = detect[1]
    trad = []
    if idiom == True:
        print("human readable")
        for i in string:
            for x in i:
                for j in abctomor:
                    if x == j:
                        trad.append(abctomor[j])
                        print(f"{x} = {j}")
                trad.append(" ")
    else:
        print("morse")
        for i in string:
            for j in mortoabc:
                if i == j:
                    trad.append(mortoabc[j])
                    print(f"{i} = {j}")
        trad.append(" ")
    return "".join(trad)

print(traduction(detection("caca de vaca")))
print(traduction(detection("-.-. .- -.-. .- -.. . ...- .- -.-. .-")))