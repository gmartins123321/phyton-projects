def main():
    mensagem_introdutoria()
    
    while True:
        menu()
        escolha = input("Insira sua escolha (1/2/3): ")
        
        if escolha == "3":
            print("Saindo do programa. Até logo!")
            break
        
        if escolha not in ["1", "2"]:
            print("Escolha inválida. Tente novamente.")
            continue
        
        try:
            ladoA = float(input("Insira o comprimento do lado A: "))
            ladoB = float(input("Insira o comprimento do lado B: "))
            ladoC = float(input("Insira o comprimento do lado C: "))
        except ValueError:
            print("Por favor, insira valores numéricos válidos.")
            continue
        
        if not eh_triangulo_valido(ladoA, ladoB, ladoC):
            print("Os comprimentos inseridos não formam um triângulo válido. Tente novamente.")
            continue
        
        print(f"O triângulo é {tipo_triangulo(ladoA, ladoB, ladoC)}.")
        
        if escolha == "1":
            area = calcular_area(ladoA, ladoB, ladoC)
            print(f"A área do triângulo é: {area:.2f}")
        
        elif escolha == "2":
            anguloA, anguloB, anguloC = calcular_angulos(ladoA, ladoB, ladoC)
            print(f"Os ângulos do triângulo são: A = {anguloA:.2f}°, B = {anguloB:.2f}°, C = {anguloC:.2f}°")
        
        continuar = input("Deseja realizar outra operação? (s/n): ").lower()
        if continuar != 's':
            print("Saindo do programa. Até logo!")
            break

if __name__ == "__main__":
    main()