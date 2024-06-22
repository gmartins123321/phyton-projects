import random

# Passo 1: Gerar o número secreto
int numeroaleatorio = (int) (math.random() * 100 + 1);


print("Bem-vindo ao jogo de adivinhar o número secreto!")
print("Tente adivinhar o número secreto entre 1 e 100.")
print(f"Você tem {tentativas_restantes} tentativas.")

# Passo 3: Interação com o utilizador
while tentativas_restantes > 0:
    palpite = input("Digite o seu palpite: ")

    # Verificar se a entrada é um número válido
    if not palpite.isdigit():
        print("Por favor, insira um número válido entre 1 e 100.")
        continue

    palpite = int(palpite)

    if palpite < 1 or palpite > 100:
        print("Por favor, insira um número entre 1 e 100.")
        continue

    # Passo 4: Lógica de controle
    tentativas_restantes -= 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você adivinhou o número secreto {numero_secreto} em {7 - tentativas_restantes} tentativas.")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior do que o seu palpite.")
    else:
        print("O número secreto é menor do que o seu palpite.")

    if tentativas_restantes > 0:
        print(f"Você tem {tentativas_restantes} tentativas restantes.")
    else:
        print(f"Você ficou sem tentativas! O número secreto era {numero_secreto}.")

print("Fim do jogo. Obrigado por jogar!")