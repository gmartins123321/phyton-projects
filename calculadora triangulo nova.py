import math

def verificar_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

def calcular_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def calcular_angulos(a, b, c):
    anguloA = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
    anguloB = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
    anguloC = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
    return anguloA, anguloB, anguloC

def classificar_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

def main():
    print("Bem-vindo à Calculadora de Triângulos.")
    
    while True:
        print("\nEscolha uma opção:")
        print("1. Calcular a área do triângulo")
        print("2. Calcular os ângulos do triângulo")
        print("3. Sair")
        opcao = input("Opção: ")

        if opcao == "3":
            print("Saindo do programa. Até logo!")
            break

        ladoA = float(input("Insira o comprimento do lado A: "))
        ladoB = float(input("Insira o comprimento do lado B: "))
        ladoC = float(input("Insira o comprimento do lado C: "))

        if not verificar_triangulo(ladoA, ladoB, ladoC):
            print("Os comprimentos inseridos não formam um triângulo válido. Tente novamente.")
            continue

        if opcao == "1":
            area = calcular_area(ladoA, ladoB, ladoC)
            print(f"A área do triângulo é: {area:.2f}")

        elif opcao == "2":
            angulos = calcular_angulos(ladoA, ladoB, ladoC)
            print(f"Os ângulos do triângulo são: A = {angulos[0]:.2f}°, B = {angulos[1]:.2f}°, C = {angulos[2]:.2f}°")

        tipo = classificar_triangulo(ladoA, ladoB, ladoC)
        print(f"O triângulo é: {tipo}")

        repetir = input("Deseja realizar outra operação? (s/n): ").lower()
        if repetir != 's':
            print("Saindo do programa. Até logo!")
            break

if __name__ == "__main__":
    main()
