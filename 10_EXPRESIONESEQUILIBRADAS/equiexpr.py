'''Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
    Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
    Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
    Expresión balanceada: { [ a * ( c + d ) ] - 5 }
    Expresión no balanceada: { a * ( c + d ) ] - 5 }'''

exp = "{ [ a * ( c + d ) ] - 5 }"
badexp = "{ a * ( c + d ) ] - 5 }"

#creamos una lista con los simbolos que queremos respetar
lcor = [ "{", "[", "(", ")", "]", "}"]

def equilibrator(xp):
    #borramos los espacios de la expesión
    xpr = xp.replace(" ", "")
    cor = []
    #añadimos cada caracter a una lista si se encuentra en nuestra lista de simbolos
    for i in xpr:
        if i in lcor:
            cor.append(i)
    print(cor)
    #recorremos los simbolos, si hay un simbolo, tiene que haber uno igual en su posición simetrica
    for i in range(0, len(cor)+1):
        #mientras recorramos la mitad de los simbolos comprobamos
        while i < ((len(cor))/2):
            print(cor[i], cor[-1-i])
            if (cor[i] == "{") and (cor[-1-i] != "}"):
                return False
            if (cor[i] == "[") and (cor[-1-i] != "]"):
                return False
            if (cor[i] == "(") and (cor[-1-i] != ")"):
                return False
            break
        #si la mitad de los simbolos han sido correctos, la otra mitad tambien ya que son simetricos
        if i >((len(cor) + 1)/2):
            return True

print(equilibrator(exp))
print(equilibrator(badexp))
