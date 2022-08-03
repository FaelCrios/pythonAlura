import adivinhacao
import forca

print("Bem vindo ao menu dos jogos..\n A seguir escolha a opção que deseja iniciar")

print("1-Adivinhação\n2-Forca")

escolha = int(input("Qual sua escolha?"))

if(escolha == 1):
    adivinhacao.jogar()
elif(escolha == 2):
    forca.jogar()