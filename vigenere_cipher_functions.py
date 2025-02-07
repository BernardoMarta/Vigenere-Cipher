ALPHABET='abcdefghijklmnopqrstuvwxyz'

def vigenere(chave,txt):
    txt_cifrado=''
    chave
    for i in range(len(txt)):
        txt_cifrado += rodar(chave[i%len(chave)],txt[i])
    return txt_cifrado

def rodar(chave2,letra):
    n=ord(letra)-ord('a')
    nova_letra = chr((n+ord(chave2)-ord('a'))%26+ord('a'))
    return nova_letra

####
def vigenere2(chave,txt):
    txt_cifrado=''
    chave = chave*1000
    for i in range(len(txt)):
        txt_cifrado += rodar2(chave[i],txt[i])
    return txt_cifrado

def rodar2(chave2,letra):
    n=ALPHABET.index(letra)
    nova_letra = ALPHABET[(n+ALPHABET.index(chave2))%26]
    return nova_letra
