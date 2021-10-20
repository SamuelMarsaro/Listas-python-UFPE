nome_1 = input()
visualizacao_1 = int(input())
nome_2 = input()
visualizacao_2 = int(input())
nome_3 = input()
visualizacao_3 = int(input())

mais_tocada = visualizacao_1
mais_tocada_nome = nome_1

if visualizacao_2 >= mais_tocada:
    mais_tocada = visualizacao_2
    mais_tocada_nome = nome_2
    if visualizacao_2 == visualizacao_1:
        mais_tocada = visualizacao_1
        mais_tocada_nome = visualizacao_1

if visualizacao_3 >= mais_tocada:
    mais_tocada = visualizacao_3
    mais_tocada_nome = nome_3
    if visualizacao_3 == visualizacao_1:
        mais_tocada = visualizacao_1
        mais_tocada_nome = nome_1
    if visualizacao_3 == visualizacao_2 and visualizacao_3 != visualizacao_1:
        mais_tocada = visualizacao_2
        mais_tocada_nome = nome_2

menos_tocada = visualizacao_1
menos_tocada_nome = nome_1

if visualizacao_2 <= menos_tocada:
    menos_tocada = visualizacao_2
    menos_tocada_nome = nome_2

if visualizacao_3 <= menos_tocada:
    menos_tocada = visualizacao_3
    menos_tocada_nome = nome_3

if (menos_tocada_nome == nome_2 and mais_tocada_nome == nome_3) or (menos_tocada_nome == nome_3 and mais_tocada_nome == nome_2):
    segunda_mais_tocada = visualizacao_1
    segunda_mais_tocada_nome = nome_1

if (menos_tocada_nome == nome_1 and mais_tocada_nome == nome_3) or (menos_tocada_nome == nome_3 and mais_tocada_nome == nome_1):
    segunda_mais_tocada = visualizacao_2
    segunda_mais_tocada_nome = nome_2

if (menos_tocada_nome == nome_1 and mais_tocada_nome == nome_2) or (menos_tocada_nome == nome_2 and mais_tocada_nome == nome_1):
    segunda_mais_tocada = visualizacao_3
    segunda_mais_tocada_nome = nome_3

print(mais_tocada_nome, mais_tocada)
print(segunda_mais_tocada_nome, segunda_mais_tocada)
print(menos_tocada_nome, menos_tocada)
