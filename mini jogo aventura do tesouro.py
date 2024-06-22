def narrativa_inicial():
    print("Você é um explorador em busca de um tesouro lendário em uma ilha misteriosa.")
    print("Depois de dias navegando, você finalmente avista a ilha ao longe.")
    print("Você desembarca na praia e começa sua aventura.")

def selva():
    print("Você entra na selva densa.")
    escolha = input("Você ouve um barulho estranho. Você decide investigar ou continuar seu caminho? (investigar/continuar): ").lower()
    if escolha == "investigar":
        print("Você encontra um animal selvagem e se fere, mas consegue fugir.")
        return "ferido"
    else:
        print("Você encontra um caminho seguro pela selva.")
        return "seguro"

def ponte():
    print("Você se depara com uma ponte instável sobre um rio.")
    escolha = input("Você decide cruzar a ponte ou procurar outro caminho? (cruzar/procurar): ").lower()
    if escolha == "cruzar":
        print("A ponte quebra e você cai no rio, mas consegue nadar até a margem.")
        return "molhado"
    else:
        print("Você encontra um caminho seguro para atravessar o rio.")
        return "seguro"

def caverna():
    print("Você encontra a entrada de uma caverna escura.")
    escolha = input("Você decide entrar na caverna ou continuar explorando a ilha? (entrar/continuar): ").lower()
    if escolha == "entrar":
        print("Dentro da caverna, você encontra o tesouro lendário!")
        return "tesouro"
    else:
        print("Você continua explorando a ilha, mas não encontra mais nada.")
        return "perdido"

def jogo():
    narrativa_inicial()
    estado = "explorando"

    while estado != "tesouro" and estado != "perdido":
        print("\nVocê se depara com três opções:")
        print("1. Entrar na selva")
        print("2. Cruzar a ponte")
        print("3. Explorar a caverna")
        escolha = input("O que você decide fazer? (selva/ponte/caverna): ").lower()

        if escolha == "selva":
            estado = selva()
        elif escolha == "ponte":
            estado = ponte()
        elif escolha == "caverna":
            estado = caverna()
        else:
            print("Escolha inválida. Tente novamente.")

        if estado == "ferido":
            print("Você está muito ferido e não consegue continuar.")
            estado = "perdido"
        elif estado == "molhado":
            print("Você está molhado e cansado, mas continua.")
            estado = "explorando"
        elif estado == "seguro":
            print("Você está seguro e continua explorando.")
            estado = "explorando"

    if estado == "tesouro":
        print("\nParabéns! Você encontrou o tesouro lendário!")
    else:
        print("\nSua aventura termina aqui. Melhor sorte na próxima vez!")

if __name__ == "__main__":
    jogo()
