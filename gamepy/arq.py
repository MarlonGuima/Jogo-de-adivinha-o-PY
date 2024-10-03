import random

def jogo_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação!")

    numero_secreto = random.randint(1,100)

    tentativas = 0
    acerto = False

    while not acerto:

        palpite = int(input("Digite um numero de 1 a 100: "))
        tentativas += 1 

        if palpite < numero_secreto:
            print("O numero secreto é maior.")
        elif palpite > numero_secreto:
            print("O numero secreto é menor.")
        else:
            print(f"Parabens, Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            acerto = True

jogo_adivinhacao()