from functools import total_ordering
from os import system
import random


def abertura():
    print("BEM VINDO AO JOGO DA FORCA!")
    system("pause")
    system("cls")

def leitura_arquivo():
    arquivo = open("lista.txt","r")
    palavras=[]
    
    for linha in arquivo:
        linha = linha.strip()  
        palavras.append(linha)            
    
    arquivo.close()
    
    numero = random.randrange(0,len(palavras))    
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def jogar():
    
    abertura()
    palavra_secreta = leitura_arquivo()
    letras_acertadas= inicializa_letras_acertadas(palavra_secreta)
    
    enforcou = False
    acertou = False
    erro = 0
    
    print(letras_acertadas)
    
    while(not enforcou and not acertou):
        chute = input("Entre com uma letra:  ")
        chute = chute.strip().upper()
        
        if(chute in palavra_secreta):        
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    print("Encontrei o teu chute: {} na posicao {}".format(chute, index+1))
                    letras_acertadas[index] = chute
                    #print(letras_acertadas)               
                index+=1
        else:
            erro += 1
        
        enforcou = erro == 6
        acertou = "_" not in letras_acertadas
        
        print(letras_acertadas)        
        
    if(acertou):
        print("Parabéns você acertou a palavra secreta")
        system("pause")
        system("cls")  
    else:  
        print("fim de jogo, voce perdeu !")
        system("pause")
        system("cls")


if(__name__ == "__main__"):
    jogar()
    