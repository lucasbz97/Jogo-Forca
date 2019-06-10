import adv
import Forca

def escolhe_jogo():
    print("***************************")
    print("***Escolha seu jogo***")
    print("***************************")

    print("1 - Adivinhação, 2 - Forca")
    jogo = int(input())

    if(jogo == 1):
        print("Jogando Adivinhação")
        adv.jogar()
    else:
        print("Jogando Forca")
        Forca.jogarForca()

if(__name__ == "__main__"):
    escolhe_jogo()
