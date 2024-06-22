import random

def escolher_caminho():
    print("Bem-vindo à Escolha do Caminho!")
    print("Você tem três opções de caminho:")
    print("1. Caminho A")
    print("2. Caminho B")
    print("3. Caminho C")
    
    escolha = input("Digite o nome ou a letra correspondente ao caminho escolhido (A, B ou C): ").strip().upper()
    
    if escolha == 'A' or escolha == 'CAMINHO A':
        print("Escolheu o Caminho A: É um caminho seguro e tranquilo!")
    elif escolha == 'B' or escolha == 'CAMINHO B':
        print("Escolheu o Caminho B: Este caminho está cheio de desafios e aventuras!")
    elif escolha == 'C' or escolha == 'CAMINHO C':
        print("Escolheu o Caminho C: Um caminho misterioso e imprevisível!")
    else:
        print("Escolha inválida. Tente novamente.")
        escolher_caminho()  # Rechama a função para uma nova tentativa

def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 5
    print("\nAgora, vamos jogar um jogo de adivinhação!")
    print(f"Eu escolhi um número secreto entre 1 e 100. Você tem {tentativas} tentativas para adivinhar.")
    
    while tentativas > 0:
        palpite = int(input("Qual é o seu palpite? "))
        
        if palpite < numero_secreto:
            tentativas -= 1
            print(f"Errado! O número secreto é maior. Você tem {tentativas} tentativas restantes.")
        elif palpite > numero_secreto:
            tentativas -= 1
            print(f"Errado! O número secreto é menor. Você tem {tentativas} tentativas restantes.")
        else:
            print("Parabéns! Você adivinhou o número secreto!")
            break
        
        if tentativas == 0:
            print(f"Você não tem mais tentativas. O número secreto era {numero_secreto}.")

def main():
    escolher_caminho()
    adivinhar_numero()

if __name__ == "__main__":
    main()