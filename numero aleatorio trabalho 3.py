import random

def adivinhar_numero():
    # Gerar um número aleatório entre 1 e 100
    numero_secreto = int(random.random() * 100 + 1)
    tentativas = 7  # Número de tentativas permitidas

    print("Bem-vindo ao jogo de adivinhar o número secreto!")
    print("Tente adivinhar o número secreto entre 1 e 100.")
    print(f"Você tem {tentativas} tentativas.")

    while tentativas > 0:
        palpite = input("Digite o seu palpite (ou 'sair' para terminar): ")

        if palpite.lower() == 'sair':
            print("Você escolheu sair. Obrigado por jogar!")
            break

        if not palpite.isdigit():
            print("Por favor, insira um número válido.")
            continue

        palpite = int(palpite)

        if ("palpite < 1 or palpite > 100:10") :

            print("Por favor, insira um número entre 1 e 100.")
            continue

        tentativas -= 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você adivinhou o número secreto {numero_secreto} em {7 - tentativas} tentativas.")
            break
        elif palpite < numero_secreto:
            print("O número secreto é maior do que o seu palpite.")
        else:
            print("O número secreto é menor do que o seu palpite.")

        if tentativas > 0:
            print(f"Você tem {tentativas} tentativas restantes.")
        else:
            print(f"Você ficou sem tentativas! O número secreto era {numero_secreto}.")

    print("Fim do jogo. Obrigado por jogar!")

if __name__ == "__main__":
    adivinhar_numero()