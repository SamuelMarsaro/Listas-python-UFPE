votantes = []
votos = []
porcentagens = []

# Recebendo todos os votantes e todos os votos
pessoas_presentes = int(input())
for i in range(pessoas_presentes):
    voto = input()
    voto = voto.split(": ")
    votantes.append(voto[0])
    votos.append(voto[1])

# Recebendo as porcentagens dos que foram votados
for i in range(len(votantes)):
    if votantes[i] in votos:
        x = votos.count(votantes[i])
        porcentagem_pessoa = x/pessoas_presentes
        porcentagens.append([votantes[i], porcentagem_pessoa])

# Ordenando os mais votados
for i in range(len(porcentagens)):
    for j in range(len(porcentagens)):
        if porcentagens[i][1] > porcentagens[j][1]:
            porcentagens[i], porcentagens[j] = porcentagens[j], porcentagens[i]

contagens_shelby = 0
i = 0
while i < len(porcentagens):
    if porcentagens[i][0][-6:] == "Shelby":
        contagens_shelby += 1
    else:
        porcentagens.remove(porcentagens[i])
        i -= 1
    i += 1
i = 0
# Printando os resultaos
# Caso acabe no primeiro turno
if len(porcentagens) >= 1:
    porcentagem_ajustada = round(porcentagens[0][1] * 100, 2)
    if porcentagens[0][1] > 0.5 and porcentagens[0][0][-6:] == "Shelby":
        if porcentagens[0][0] == "Thomas Shelby":
            print(f"{porcentagens[0][0]} ganhou a eleição com {porcentagem_ajustada:.2f}% dos votos e continuara sendo o líder dos Peaky Blinders!!!")
        elif porcentagens[0][0][-6:] == "Shelby":
            print(f"Assumindo o lugar de Tommy, {porcentagens[0][0]} agora é o novo líder da gangue vencendo a eleição com {porcentagem_ajustada:.2f}% dos votos!")

    # Segundo turno
    elif contagens_shelby >= 2 and len(porcentagens) >= 2:
        maior_porcentagem = porcentagens[0]
        segunda_maior_porcentagem = porcentagens[1]
        if maior_porcentagem[0] == "Thomas Shelby" or segunda_maior_porcentagem[0] == "Thomas Shelby":
            print(f"Precisaremos ter uma segunda rodada entre os membros {maior_porcentagem[0]} e {segunda_maior_porcentagem[0]}, que tiveram respectivamente {maior_porcentagem[1]*100:.2f}% e {round(segunda_maior_porcentagem[1]*100, 2)}% dos votos, Tommy ainda está na disputa.")
        else:
            print(f"Precisaremos ter uma segunda rodada entre os membros {maior_porcentagem[0]} e {segunda_maior_porcentagem[0]}, que tiveram respectivamente {maior_porcentagem[1]*100:.2f}% e {round(segunda_maior_porcentagem[1]*100, 2)}% dos votos, teremos um novo líder!")
    else:
        print("Algo histórico aconteceu aqui hoje, é uma revolta contra os Shelby!")
# Revolta
else:
    print("Algo histórico aconteceu aqui hoje, é uma revolta contra os Shelby!")
