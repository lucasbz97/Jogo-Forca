import random

def jogar():
    print("***************************")
    print("***Jogo de adivinhação***")
    print("***************************")
    pontos = 1000



    print("Escolha o nível de dificuldade: "
          "1 - fácil, 2 - médio, 3 - dificil")
    nivel = int(input())

    if(nivel == 1):
        vezes = 20
    elif(nivel == 2):
        vezes = 10
    elif(nivel == 3):
        vezes = 5
    else:
        print("Número inválido")

    num_secreto = random.randrange(1,101)
    rodada = 1

    for rodada in range(1,vezes+1):
        print("Rodada {} de {} ".format(rodada,vezes))
        par = num_secreto%2 == 0

        if(par):
            print("Dica: O número secreto é par")
        else:
            print("O valor é ímpar")
        chute = int(input("Digite o numero: "))


        if (chute < 1 or chute > 100):
            print("Valor inválido, digite um valor maior que zero e menor que 100!")
            continue


        if (num_secreto == chute):
            print("\nAcertoou")
            print("Sua pontuação foi de {} !".format(pontos))
            break
        elif (num_secreto > chute):
            print("ERRROOOOOUUU, seu chute deve ser MAIOR")
        else:
            print("ERRROOOOOUUU, seu chute deve ser MENOR")
            pontos = pontos - round(abs(((num_secreto - chute) /3)))
        rodada = rodada+1

    print("O número secreto era: ", num_secreto)
    print("\n*************")
    print("Acaboooooou")
    print("*************")

if (__name__ == "__main__"):
    jogar()

