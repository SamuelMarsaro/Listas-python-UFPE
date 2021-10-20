nome_musica_1, artista_1, tempo_1 = input().split(" - ")
nome_musica_2, artista_2, tempo_2 = input().split(" - ")
nome_musica_3, artista_3, tempo_3 = input().split(" - ")
nome_musica_4, artista_4, tempo_4 = input().split(" - ")
nome_musica_5, artista_5, tempo_5 = input().split(" - ")
nome_musica_6, artista_6, tempo_6 = input().split(" - ")

tempo_joao_gomes = 0
tempo_ze_vaqueiro = 0
musicas_joao_gomes = 0
musicas_ze_vaqueiro = 0

if artista_1 == "Joao gomes":
    tempo_joao_gomes += float(tempo_1) * 60
    musicas_joao_gomes += 1
elif artista_1 == "Ze vaqueiro":
    tempo_ze_vaqueiro += float(tempo_1) * 60
    musicas_ze_vaqueiro += 1

if artista_2 == "Joao gomes":
    tempo_joao_gomes += float(tempo_2) * 60
    musicas_joao_gomes += 1
elif artista_2 == "Ze vaqueiro":
    tempo_ze_vaqueiro += float(tempo_2) * 60
    musicas_ze_vaqueiro += 1

if artista_3 == "Joao gomes":
    tempo_joao_gomes += float(tempo_3) * 60
    musicas_joao_gomes += 1
elif artista_3 == "Ze vaqueiro":
    tempo_ze_vaqueiro += float(tempo_3) * 60
    musicas_ze_vaqueiro += 1

if artista_4 == "Joao gomes":
    tempo_joao_gomes += float(tempo_4) * 60
    musicas_joao_gomes += 1
elif artista_4 == "Ze vaqueiro":
    tempo_ze_vaqueiro += float(tempo_4) * 60
    musicas_ze_vaqueiro += 1

if artista_5 == "Joao gomes":
    tempo_joao_gomes += float(tempo_5) * 60
    musicas_joao_gomes += 1
elif artista_5 == "Ze vaqueiro":
    tempo_ze_vaqueiro += float(tempo_5) * 60
    musicas_ze_vaqueiro += 1

if artista_6 == "Joao gomes":
    tempo_joao_gomes += float(tempo_6) * 60
    musicas_joao_gomes += 1
elif artista_6 == "Ze vaqueiro":
    tempo_ze_vaqueiro += float(tempo_6) * 60
    musicas_ze_vaqueiro += 1

if musicas_ze_vaqueiro != 0 and musicas_joao_gomes != 0:
    media_ze_vaqueiro = tempo_ze_vaqueiro / musicas_ze_vaqueiro
    media_joao_gomes = tempo_joao_gomes / musicas_joao_gomes

    if media_joao_gomes == media_ze_vaqueiro:
        print("Tivemos um empate tecnico.")
    elif media_joao_gomes > media_ze_vaqueiro:
        print(
            "De acordo com estes dados temos um forte indicativo de que as musicas de Joao gomes sao mais longas que as de Ze vaqueiro.")

    elif media_ze_vaqueiro > media_joao_gomes:
        print(
            "De acordo com estes dados temos um forte indicativo de que as musicas de Ze vaqueiro sao mais longas que as de Joao gomes.")

elif musicas_ze_vaqueiro == 0 or musicas_joao_gomes == 0:
    print("Nao tivemos dados suficientes para chegar uma conclusao.")