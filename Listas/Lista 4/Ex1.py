NUMERO_VELOCISTAS = 5
lista_ordenada = list()

# Criando uma lista com o mesmo numero de elementos
for i in range(NUMERO_VELOCISTAS):
    lista_ordenada.append("")

# Loop para receber os valores
for i in range(NUMERO_VELOCISTAS):
    velocista_posicao = input()
    velocista_posicao = velocista_posicao.split("-")
    lista_ordenada[int(velocista_posicao[1]) - 1] = velocista_posicao[0]

# Printar resultados
print("Velocista - Posicao\n")
for i in range(len(lista_ordenada)):
    print(f"{lista_ordenada[i]}- {i+1}")
