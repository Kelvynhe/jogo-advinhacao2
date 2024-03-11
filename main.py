import random


def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    escolha = 0
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while int(escolha) != 1 and int(escolha) != 2 and int(escolha) != 3:
        escolha = input("Selecione a dificuldade \n 1 - Facil \n 2 - Médio \n 3 - Dificil \n")
        if int(escolha) == 3:
            tentativas = 2
        elif int(escolha) == 2:
            tentativas = 4
        elif int(escolha) == 1:
            tentativas = 8
        else: 
            print("Selecione um número de tentativas válido! ")

    print(f"Você tem {tentativas} tentativas.")

    while tentativas > 0:
        chute = int(input("Digite seu chute: "))

        if chute < numero_secreto:
            print("O número secreto é maior.")
        elif chute > numero_secreto:
            print("O número secreto é menor.")
        else:
            print("Parabéns! Você acertou!")
            return

        tentativas -= 1
        if tentativas > 0:
            print(f"Você tem mais {tentativas} tentativas.")

    print("Suas tentativas acabaram. O número secreto era:", numero_secreto)


jogo_adivinhacao()