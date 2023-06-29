
#1.2.1

def corrigir_palavra(letras):
    if not isinstance(letras, str):
        raise ValueError("argumento inválido")
    car = 0
    while car < len(letras)-1:
        if (letras[car].isupper() and letras[car].lower() == letras[car+1]) or (
            letras[car].islower() and letras[car].upper() == letras[car+1]):
            letras = letras.replace(letras[car] + letras[car+1], '')
        elif True:
            car += 1
        else:
            car = 0
    return letras


#1.2.2

def eh_anagrama(palavra1,palavra2):
    
    if not isinstance(palavra1,str) or not isinstance(palavra2,str):
        raise ValueError("argumento inválido")
    
    palavra1=palavra1.lower()
    palavra2=palavra2.lower()
    
    if len(palavra1) != len(palavra2):
        return False
    counter = 0
    for car in range(len(palavra1)):
        if palavra1[car] in palavra2:
            counter +=1
    if counter == len(palavra1):
        return True
    else:
        return False

'''def corrigir_doc(texto):
    if not isinstance(texto, str):
        raise ValueError("argumento inválido")
    elif string.punctuation in texto:
        raise ValueError("argumento inválido")'''


#2.2.1

def obter_posicao(letra, num):
    if (letra == 'C' and num in (1,2,3)) or (        #esta condicao verifica os limites de cada movimento
        letra == 'B' and num in (7,8,9)) or (
            letra == 'E' and num in (1,4,7)) or (
                letra == 'D' and num in (3,6,9)):
        return num 
    dic = {'C':num-3, 'B': num+3, 'E': num-1, 'D': num+1}
    return dic[letra]
print(obter_posicao('C',2))

#2.2.2

def obter_digito(letras, num):
    for letra in letras:
        num = obter_posicao(letra,num)
    return num
print(obter_digito('CEBB',5))

#2.2.3
t = ('CEE','DDBBB','ECDBE', 'CCCCB')
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
print(obter_pin(t))




        


        

