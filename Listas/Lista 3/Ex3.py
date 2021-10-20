voltas = int(input())
j = 0
soma_total = 0

while j < voltas:
    nota_1 = int(input())
    nota_2 = int(input())
    nota_3 = int(input())
    nota_4 = int(input())
    nota_5 = int(input())
    soma_notas = nota_1 + nota_2 + nota_3 + nota_4 + nota_5
    if j == 0:
        pontuacao_final = soma_notas
    elif soma_notas > pontuacao_final:
        pontuacao_final = soma_notas
    print(f"A pontuacao na volta {j + 1} foi de {soma_notas} pontos!")
    j += 1
else:
    print(f"A pontuacao final de Rayssa foi de {pontuacao_final} pontos!")
