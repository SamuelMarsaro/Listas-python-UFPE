GAP, BARSPIN, SUPERHOMEM, ROTACAO360, ROTACAO720, ROTACAO1080, BACKFLIP, FRONTFLIP = 10, 30, 100, 50, 150, 400, 250, 500

jogadores = int(input())
manobra = ""
for i in range(jogadores):
    manobra = ""
    pontuacao_jogador = 0
    nome = input()
    while manobra != "Fim":
        manobra = input()
        if manobra == "Gap":
            pontuacao_jogador += GAP
        if manobra == "Barspin":
            pontuacao_jogador += BARSPIN
        if manobra == "Superhomem":
            pontuacao_jogador += SUPERHOMEM
        if manobra == "Rotacao de 360":
            pontuacao_jogador += ROTACAO360
        if manobra == "Rotacao de 720":
            pontuacao_jogador += ROTACAO720
        if manobra == "Rotacao de 1080":
            pontuacao_jogador += ROTACAO1080
        if manobra == "Backflip":
            pontuacao_jogador += BACKFLIP
        if manobra == "Frontflip":
            pontuacao_jogador += FRONTFLIP

    if i == 0:
        campeao = nome
        melhor_nota = pontuacao_jogador
    elif i == 1:
        if pontuacao_jogador > melhor_nota:
            segundo_colocado = campeao
            segunda_nota = melhor_nota
            campeao = nome
            melhor_nota = pontuacao_jogador
        elif pontuacao_jogador <= melhor_nota:
            segundo_colocado = nome
            segunda_nota = pontuacao_jogador
    elif i >= 2:
        if pontuacao_jogador < melhor_nota and pontuacao_jogador <= segunda_nota:
            terceiro_colocado = nome
            terceira_nota = pontuacao_jogador
        elif pontuacao_jogador > segunda_nota and pontuacao_jogador <= melhor_nota:
            terceiro_colocado = segundo_colocado
            terceira_nota = segunda_nota
            segundo_colocado = nome
            segunda_nota = pontuacao_jogador
        elif pontuacao_jogador > melhor_nota:
            terceiro_colocado = segundo_colocado
            terceira_nota = segunda_nota
            segundo_colocado = campeao
            segunda_nota = melhor_nota
            campeao = nome
            melhor_nota = pontuacao_jogador

print(campeao)
print(melhor_nota)
print(segundo_colocado)
print(segunda_nota)
print(terceiro_colocado)
print(terceira_nota)
