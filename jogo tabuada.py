import random


def exibir_mensagem_introducao():
    print("Bem-vindo ao Tabuadex!")
    print("Regras do jogo:")
    print("1. Você receberá problemas de tabuada aleatórios.")
    print("2. Para cada resposta correta, você ganha 10 pontos.")
    print("3. Se desejar sair do jogo, digite 'sair'.")
    print("Vamos começar!\n")
    import random

def gerar_problema():
    multiplicador = random.randint(1, 9)
    base = random.randint(1, 9)
    return base, multiplicador

def obter_resposta_usuario(base, multiplicador):
    resposta = input(f"Qual é o resultado de {base} x {multiplicador}? ")
    return resposta

def verificar_resposta(base, multiplicador, resposta_usuario):
    resposta_correta = base * multiplicador
    return resposta_correta == int(resposta_usuario)
def main():
    pontos = 0
    exibir_mensagem_introducao()
    
    while True:
        base, multiplicador = gerar_problema()
        resposta_usuario = obter_resposta_usuario(base, multiplicador)
        
        if resposta_usuario.lower() == 'sair':
            break
        
        try:
            if verificar_resposta(base, multiplicador, resposta_usuario):
                pontos += 10
                print("Correto! Você ganhou 10 pontos.")
            else:
                print(f"Errado! A resposta correta era {base * multiplicador}.")
        except ValueError:
            print("Por favor, insira um número válido.")
        
        print(f"Seu total de pontos: {pontos}\n")
    
    print(f"Fim de jogo! Seu total final de pontos: {pontos}")

if __name__ == "__main__":
    main()
