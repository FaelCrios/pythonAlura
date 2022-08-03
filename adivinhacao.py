from functools import total_ordering
from os import system
import random


def jogar():
    print("Bem vindo ao jogo")
    print("Tente acertar o numero gerado")
    system("pause")
    system("cls")
    numero_secreto=random.randrange(1,101)
    int(numero_secreto)

    print("Antes de tudo começar...\n Vamos definir o nível do jogo")
    print("1- Fácil\n2- Médio\n3- Dificil\n4- Impossivel")
    nivel = int(input("Entre com a resposta.. "))
    system("pause")
    system("cls")
    numero_tentativas = 0
    #total_tentativas = 3

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    elif(nivel == 3):
        total_tentativas = 5
    elif(nivel == 4):
        total_tentativas = 1
    else:
        print("Resposta Errada mané")
        system("pause")
        exit()

    for numero_tentativas in range(1, total_tentativas+1):
        print("Esta é a rodada {} de {}".format(numero_tentativas, total_tentativas))
        chute = input("Digite o numero: ")
        numero = int(chute)
        if(numero == numero_secreto):
            print("Voce digitou :",numero,"e está correto")
            exit()
        else:
            if(numero > numero_secreto):
                print("Voce digitou :",numero," o numero que vc inseriu é maior que o secreto")
                system("pause")
                system("cls")
            elif(numero < numero_secreto):
                print("Voce digitou :",numero," o numero que vc inseriu é menor que o secreto")
                system("pause")
                system("cls")
                
        
    print("Perdeu o numero secreto é: ", numero_secreto)
    
if(__name__ == "__main__"):
    jogar()
        