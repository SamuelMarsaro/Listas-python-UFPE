movimento_1 = input()
continuar_programa = "sim"

if movimento_1 != "cima" and movimento_1 != "baixo" and movimento_1 != "esquerda" and movimento_1 != "direita":
    print("O jogador não fez nenhuma entrada valida")
    continuar_programa = "nao"

if continuar_programa == "sim":
    movimento_2 = input()

    if (movimento_1 == "cima" or movimento_1 == "baixo") and (movimento_2 == "baixo" or movimento_2 == "cima"):
        print("O jogador fez somente 1 movimento(s)")
        continuar_programa = "nao"

    elif (movimento_1 == "direita" or movimento_1 == "esquerda") and (movimento_2 == "direita" or movimento_2 == "esquerda"):
        print("O jogador fez somente 1 movimento(s)")
        continuar_programa = "nao"

    elif movimento_2 != "cima" and movimento_2 != "baixo" and movimento_2 != "esquerda" and movimento_2 != "direita":
        print("O jogador fez 1 movimento(s) e tentou uma entrada invalida")
        continuar_programa = "nao"

    if continuar_programa == "sim":
        movimento_3 = input()

        if (movimento_2 == "cima" or movimento_2 == "baixo") and (movimento_3 == "baixo" or movimento_3 == "cima"):
            print("O jogador fez somente 2 movimento(s)")
            continuar_programa = "nao"

        elif (movimento_2 == "direita" or movimento_2 == "esquerda") and (movimento_3 == "direita" or movimento_3 == "esquerda"):
            print("O jogador fez somente 2 movimento(s)")
            continuar_programa = "nao"

        elif movimento_3 != "cima" and movimento_3 != "baixo" and movimento_3 != "esquerda" and movimento_3 != "direita":
            print("O jogador fez 2 movimento(s) e tentou uma entrada invalida")
            continuar_programa = "nao"

        if continuar_programa == "sim":
            movimento_4 = input()

            if (movimento_3 == "cima" or movimento_3 == "baixo") and (movimento_4 == "baixo" or movimento_4 == "cima"):
                print("O jogador fez somente 3 movimento(s)")
                continuar_programa = "nao"

            elif (movimento_3 == "direita" or movimento_3 == "esquerda") and (movimento_4 == "direita" or movimento_4 == "esquerda"):
                print("O jogador fez somente 3 movimento(s)")
                continuar_programa = "nao"

            elif movimento_4 != "cima" and movimento_4 != "baixo" and movimento_4 != "esquerda" and movimento_4 != "direita":
                print("O jogador fez 3 movimento(s) e tentou uma entrada invalida")
                continuar_programa = "nao"

            if continuar_programa == "sim":
                movimento_5 = input()

                if (movimento_4 == "cima" or movimento_4 == "baixo") and (movimento_5 == "baixo" or movimento_5 == "cima"):
                    print("O jogador fez somente 4 movimento(s)")
                    continuar_programa = "nao"

                elif (movimento_4 == "direita" or movimento_4 == "esquerda") and (movimento_5 == "direita" or movimento_5 == "esquerda"):
                    print("O jogador fez somente 4 movimento(s)")
                    continuar_programa = "nao"

                elif movimento_5 != "cima" and movimento_5 != "baixo" and movimento_5 != "esquerda" and movimento_5 != "direita":
                    print("O jogador fez 4 movimento(s) e tentou uma entrada invalida")
                    continuar_programa = "nao"

if continuar_programa == "sim":
    print("O jogador conseguiu fazer todos 5 movimentos com sucesso!")