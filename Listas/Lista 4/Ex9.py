n_casos  = int(input())
casos = []

# Recebendo todos os casos
for i in range(n_casos):
    caso = input()
    caso = caso.split(" ")
    casos.append(caso)

casos_mike, casos_harvey, casos_louis = 0, 0, 0
pontuacao_mike, pontuacao_harvey, pontuacao_louis = 0, 0, 0
pro_bonos_mike, pro_bonos_harvey, pro_bonos_louis = 0, 0, 0
pontuacao_mike_maxima, pontuacao_harvey_maxima, pontuacao_louis_maxima = 0, 0, 0

# Calculando médias e casos máximos
for i in range(len(casos)):
    if casos[i][0] == "Mike":
        pontuacao_mike += int(casos[i][2])
        casos_mike += 1
        if int(casos[i][2]) > pontuacao_mike_maxima:
            pontuacao_mike_maxima = int(casos[i][2])
        if casos[i][1] == "pro-bono":
            pro_bonos_mike += 1
    elif casos[i][0] == "Harvey":
        pontuacao_harvey += int(casos[i][2])
        casos_harvey += 1
        if int(casos[i][2]) > pontuacao_harvey_maxima:
            pontuacao_harvey_maxima = int(casos[i][2])
        if casos[i][1] == "pro-bono":
            pro_bonos_harvey += 1
    elif casos[i][0] == "Louis":
        pontuacao_louis += int(casos[i][2])
        casos_louis += 1
        if int(casos[i][2]) > pontuacao_louis_maxima:
            pontuacao_louis_maxima = int(casos[i][2])
        if casos[i][1] == "pro-bono":
            pro_bonos_louis += 1

media_mike = pontuacao_mike/casos_mike
media_harvey = pontuacao_harvey/casos_harvey
media_louis = pontuacao_louis/casos_louis

# Ordenando 
final = [["Mike", media_mike, pro_bonos_mike, pontuacao_mike_maxima], ["Louis", media_louis, pro_bonos_louis, pontuacao_louis_maxima], ["Harvey", media_harvey, pro_bonos_harvey, pontuacao_harvey_maxima]]

for i in range(len(final)):
    for j in range(len(final)):
        if final[i][1] > final[j][1]:
            final[i], final[j] = final[j], final[i]

if final[0][1] == final[1][1] == final[0][1]:
    for i in range(len(final)):
        for j in range(len(final)):
            if final[i][2] > final[j][2]:
                final[i], final[j] = final[j], final[i]

elif final[0][1] == final[1][1] != final[2][1]:
    if final[0][2] > final[1][2]:
        final[0], final[1] = final[1], final[0]

elif final[0][1] != final[1][1] == final[2][1]:
    if final[2][2] > final[1][2]:
        final[2], final[1] = final[1], final[2]

if final[0][1] == final[1][1] == final[0][1] or final[0][1] == final[1][1] != final[2][1] or final[0][1] != final[1][1] == final[2][1]:
    if final[0][2] == final[1][2] == final[2][2]:
        for i in range(len(final)):
            for j in range(len(final)):
                if final[i][3] > final[j][3]:
                    final[i], final[j] = final[j], final[i]

    elif final[0][2] == final[1][2] != final[2][2]:
        if final[1][3] > final[0][3]:
            final[0], final[1] = final[1], final[0]

    elif final[0][2] != final[1][2] == final[2][2]:
        if final[2][3] > final[1][3]:
            final[2], final[1] = final[1], final[2]

if final[0][1:] == final[1][1:] == final[2][1:]:
    final[0][0] = "Mike"
    final[2][0] = "Harvey"

elif final[0][1:] != final[1][1:] == final[2][1:]:
    if final[0][0] == "Mike":
        final[1][0] = "Louis"
        final[2][0] = "Harvey"
    elif final[0][0] == "Louis":
        final[1][0] = "Mike"
        final[2][0] = "Harvey"
    elif final[0][0] == "Harvey":
        final[1][0] = "Mike"
        final[2][0] = "Louis"

# PRINTANDO RESULTADOS:
print(f"Mike;\nMédia: {media_mike:.2f}\nQuantidade de Pró-bonos: {pro_bonos_mike}\nMáximo: {pontuacao_mike_maxima}\n")
print(f"Louis;\nMédia: {media_louis:.2f}\nQuantidade de Pró-bonos: {pro_bonos_louis}\nMáximo: {pontuacao_louis_maxima}\n")
print(f"Harvey;\nMédia: {media_harvey:.2f}\nQuantidade de Pró-bonos: {pro_bonos_harvey}\nMáximo: {pontuacao_harvey_maxima}\n")
print(f"Quem ganhou a competição e vai ficar com a sala nova foi o {final[0][0]}!!! E o coitado que vai ter que comprar os móveis vai ser o {final[2][0]}.")
