numero_de_partidas = int(input())

for i in range(numero_de_partidas):
    ponto_lance = 0
    s = int(input())
    l = int(input())
    atacante = input()
    sacador = input()
    if (s**3) % 3 == 0:
        ponto_lance += 1
        print(f"AAAAACE! ELE MESMO, {sacador}! UMA FERA! UMA BESTA ENJAULADA")
    elif s % 2 == 0:
        ponto_lance += 1
        print(f"Saque pra fora do {sacador}, que desperdicio de uma bela oportunidade!!!")
    else:
        print(f"Bom saque do {sacador}, bola em jogo!")
        k = (l ** (1/3))
        n = round(k)
        if (k - n) < 0:
            n -= 1
        if n % 2 == 0:
            print(f"Levantamento longo na lateral para o {atacante} finalizar")
        else:
            print(f"Levantamento rápido com maestria no meio para o {atacante} finalizar")

        if s >= l:
            ponto_lance += 1
            print("“NÃO! NÃO É ASSIM...")
        else:
            print(f"Bom ataque do {atacante}! momento decisivo!")
            if (s + l) % 2 == 0:
                print("A bola volta para o campo do Brasil, recomeça o lance!")
            else:
                print("É DO BRASIL!!!!")
                ponto_lance += 1

        while ponto_lance == 0:
            s = int(input())
            l = int(input())
            atacante = input()
            k = (l ** (1 / 3))
            n = round(k)
            if (k - n) < 0:
                n -= 1
            if n % 2 == 0:
                print(f"Levantamento longo na lateral para o {atacante} finalizar")
            else:
                print(f"Levantamento rápido com maestria no meio para o {atacante} finalizar")

            if s >= l:
                ponto_lance += 1
                print("“NÃO! NÃO É ASSIM...")
            else:
                print(f"Bom ataque do {atacante}! momento decisivo!")
                if (s + l) % 2 == 0:
                    print("A bola volta para o campo do Brasil, recomeça o lance!")
                else:
                    print("É DO BRASIL!!!!")
                    ponto_lance += 1
