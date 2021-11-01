entrada = ""
nomes = list()

# Recebendo e ordenando valores
while entrada != "fim":
    entrada = input()
    if entrada == "adicionar":
        nome = input()
        nomes.append(nome)
        print(f"{nome} foi adicionada ao final da lista")

    elif entrada == "remover":
        nome = input()
        nomes.remove(nome)
        print(f"{nome} foi removida da lista")

    elif entrada == "atualizar posiçao":
        nome = input()
        posicao = int(input())
        y = nomes.index(nome)

        if nome != nomes[posicao]:
            nomes.insert(posicao, nome)
            nomes.pop(y + 1)
            print(f"{nome} foi inserida na posição {posicao} da lista")
        else:
            print(f"Nada mudou, {nome} ja esta na posiçao certa")

# Printando resultados
nomes_ordenados = ""
if len(nomes) > 0:
    for i in range(len(nomes)):
        nomes_ordenados += nomes[i] + " "
    nomes_ordenados = nomes_ordenados[:-1]
    print(nomes_ordenados)
else:
    print("Não sobraram pretendentes para voce, Ted")
