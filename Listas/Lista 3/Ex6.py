baterias = int(input())

recorde_mundial = 9.58
soma_atleta_1, soma_atleta_2, soma_atleta_3, soma_atleta_4, soma_atleta_5 = 0, 0, 0, 0, 0

for i in range(baterias):
    tempo_atleta_1 = float(input())
    soma_atleta_1 += tempo_atleta_1
    if tempo_atleta_1 < recorde_mundial:
        print(f"O atleta 1 bateu o recorde mundial com o tempo: {tempo_atleta_1}")
        recorde_mundial = tempo_atleta_1

    tempo_atleta_2 = float(input())
    soma_atleta_2 += tempo_atleta_2
    if tempo_atleta_2 < recorde_mundial:
        print(f"O atleta 2 bateu o recorde mundial com o tempo: {tempo_atleta_2}")
        recorde_mundial = tempo_atleta_2

    tempo_atleta_3 = float(input())
    soma_atleta_3 += tempo_atleta_3
    if tempo_atleta_3 < recorde_mundial:
        print(f"O atleta 3 bateu o recorde mundial com o tempo: {tempo_atleta_3}")
        recorde_mundial = tempo_atleta_3

    tempo_atleta_4 = float(input())
    soma_atleta_4 += tempo_atleta_4
    if tempo_atleta_4 < recorde_mundial:
        print(f"O atleta 4 bateu o recorde mundial com o tempo: {tempo_atleta_4}")
        recorde_mundial = tempo_atleta_4

    tempo_atleta_5 = float(input())
    soma_atleta_5 += tempo_atleta_5
    if tempo_atleta_5 < recorde_mundial:
        print(f"O atleta 5 bateu o recorde mundial com o tempo: {tempo_atleta_5}")
        recorde_mundial = tempo_atleta_5

menor_tempo = soma_atleta_1
campeao = "1"

if soma_atleta_2 < menor_tempo:
    menor_tempo = soma_atleta_2
    campeao = "2"

if soma_atleta_3 < menor_tempo:
    menor_tempo = soma_atleta_3
    campeao = "3"

if soma_atleta_4 < menor_tempo:
    menor_tempo = soma_atleta_4
    campeao = "4"

if soma_atleta_5 < menor_tempo:
    menor_tempo = soma_atleta_5
    campeao = "5"

print(f"Vencedor com o menor tempo somando todas as baterias foi: Atleta {campeao}")
