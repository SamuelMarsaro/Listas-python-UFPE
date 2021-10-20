musica_1 = str(input())
musica_2 = str(input())
musica_3 = str(input())
musica_4 = str(input())
musica_5 = str(input())
acertos = 0

if musica_1 == "pelados em santos" or musica_1 == "robocop gay" or musica_1 == "vira-vira" or musica_1 == "1406" \
        or musica_1 == "mundo animal":
    acertos += 1
if musica_2 == "pelados em santos" or musica_2 == "robocop gay" or musica_2 == "vira-vira" or musica_2 == "1406" \
        or musica_2 == "mundo animal":
    acertos += 1
if musica_3 == "pelados em santos" or musica_3 == "robocop gay" or musica_3 == "vira-vira" or musica_3 == "1406" \
        or musica_3 == "mundo animal":
    acertos += 1
if musica_4 == "pelados em santos" or musica_4 == "robocop gay" or musica_4 == "vira-vira" or musica_4 == "1406" \
        or musica_4 == "mundo animal":
    acertos += 1
if musica_5 == "pelados em santos" or musica_5 == "robocop gay" or musica_5 == "vira-vira" or musica_5 == "1406" \
        or musica_5 == "mundo animal":
    acertos += 1

if acertos == 5:
    print("Parabens voce e um genio conhecedor da musica brasileira, voce merece 5 pontos")
elif acertos >= 4:
    print("Quase perfeito mano: 3 pontos")
elif acertos >= 2:
    print("Ate que tu foi bem mas nao chegou la: 1 ponto")
elif acertos >= 0:
    print("Errou feio, errou rude: 0 pontos")