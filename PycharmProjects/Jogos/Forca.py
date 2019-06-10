import random

def jogarForca():

    imprime_msg_abertura()
    palavra_secreta = ler_palavra_secreta()
    letras_acertadas = inializa_palavras_acertadas(palavra_secreta)

    enforcou = False
    acertou  = False
    erros = 0

    print("Dica:\nA palavra tem {} letras".format(letras_acertadas.__len__()))

    while (not enforcou and not acertou) :

        chute = pede_chute()
        if(chute in palavra_secreta):
            marca_chute_correto(chute,letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

#Funções

def imprime_msg_abertura():
    print("***************************")
    print("***Jogo de adivinhação***")
    print("***************************")

def ler_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for i in arquivo:
        i = i.strip()
        palavras.append(i)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].lower()
    return palavra_secreta

def inializa_palavras_acertadas(palavras):
    return ["_" for letra in palavras]

def pede_chute():
    chute = input("Digite uma letra ae ")
    chute = chute.strip().lower()
    return chute

def marca_chute_correto(chute,letras_acertadas,ler_palavra_secreta):
    index = 0
    for letra in ler_palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("GANHOU, NA SORTE!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("PERDEEEEUUUUU, você foi enforcado vacilão!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogarForca()
