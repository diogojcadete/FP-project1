#1.2.1

def corrigir_palavra(letras):
   
    car = 0
    while car < len(letras)-1:
        if letras == '':
            break
        if (letras[car].isupper() and letras[car].lower() == letras[car+1]) or (
            letras[car].islower() and letras[car].upper() == letras[car+1]):
            letras = letras.replace(letras[car] + letras[car+1], '')
            car = 0
        elif True:
            car += 1
    return letras

#1.2.2

def eh_anagrama(palavra1,palavra2):
    
    palavra1=palavra1.lower()
    palavra2=palavra2.lower()
    
    if len(palavra1) != len(palavra2):
        return False
    if palavra1 == palavra2: # Tirar duvida - é para remover palavras iguais?
        return False
    counter = 0
    for car in range(len(palavra1)):
        if palavra1[car] in palavra2:
            counter +=1
    if counter == len(palavra1):
        return True
    else:
        return False

def corrigir_doc(texto):
    if not all(x.isalpha() or x.isspace() for x in texto) or not isinstance(texto, str) or texto.count('  ') >= 1 or texto == '':
        raise ValueError("corrigir_doc: argumento inválido")
    lista = texto.split(' ')

    for i in range(len(lista)):
        lista[i] = corrigir_palavra(lista[i])
        if lista[i] == '':
            lista.remove[lista[i]]

    i = 0
    j = 1   
    while i <len(lista)-1:
        while j <len(lista):
            if eh_anagrama(lista[i], lista[j]):
                lista.remove(lista[j])
            j+=1
        i+=1
        j = i+1 
    texto = ' '.join(lista)
    return texto

#2.2.1

def obter_posicao(letra, num):
    if (letra == 'C' and num in (1,2,3)) or (        #esta condicao verifica os limites de cada movimento
        letra == 'B' and num in (7,8,9)) or (
            letra == 'E' and num in (1,4,7)) or (
                letra == 'D' and num in (3,6,9)):
        return num 
    dic = {'C':num-3, 'B': num+3, 'E': num-1, 'D': num+1}
    return dic[letra]

#2.2.2

def obter_digito(letras, num):
    for letra in letras:
        num = obter_posicao(letra,num)
    return num

#2.2.3

def obter_pin(pin):
    for letras in range(len(pin)):
        if not isinstance(pin,tuple) or not isinstance(pin[letras],str) or len(pin)>10 or len(pin)<4:
            raise ValueError("obter_pin: argumento inválido")
    pin_num = 5
    tuplo_pin = ()
    for letras in pin:
        pin_num = obter_digito(letras,pin_num)
        tuplo_pin += (pin_num,)
    return tuplo_pin

#3.2.1

def eh_entrada(bdb):
    if not isinstance(bdb, tuple) or len(bdb)!=3:
        return False
    campo = 0
    while campo <= 1:
        if not isinstance(bdb[campo],str):
            return False
        campo +=1 
    if len(bdb[0])<1 or bdb[0][0] =='-' or bdb[0][len(bdb[0])-1] == '-' or not bdb[0].islower()  :
        return False
    else: 
        for x in range(len(bdb[0])):
            if not x.isalpha() or x != '-':
                return False
    if not (len(bdb[1])==7 or bdb[1][0] == '[' or bdb[1][6] == ']'): 
        return False
    else:
        for x in range(bdb[1][1:6]):
            if not (x.isalpha() or x.islower()):
                return False
    if bdb[2]









        


        

