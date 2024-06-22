# Função para calcular a média de três notas
def calcularMedia(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

# Função para contar palavras em uma frase (implementada conforme as especificações, mesmo que não mencionadas explicitamente no enunciado)
def contarPalavras(frase):
    return len(frase.split())

# Programa principal
def main():
    print("Bem-vindo à Calculadora de Média!")
    
    # Pedir ao utilizador para inserir três notas
    nota1 = float(input("Por favor, insira a primeira nota: "))
    nota2 = float(input("Por favor, insira a segunda nota: "))
    nota3 = float(input("Por favor, insira a terceira nota: "))
    
    # Calcular a média das três notas
    media = calcularMedia(nota1, nota2, nota3)
    
    # Exibir o resultado
    print(f"A média das três notas é: {media:.2f}")

# Chamada da função principal para executar o programa
if __name__ == "__main__":
    main()
