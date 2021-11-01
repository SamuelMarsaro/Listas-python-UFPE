# Recebendo os nomes e o valor K
nomes = input()
nomes = nomes.split(" ")
K = int(input())

# Iterando com o valor K e a lista de nomes
for i in range(K):
    troca = int(input())
    nomes[troca], nomes[-(troca + 1)] = nomes[-(troca + 1)], nomes[troca]
    if nomes[troca] == nomes[-(troca + 1)]:
        print("Nenhuma troca foi feita")
    else:
        print(f"A testemunha {nomes[-(troca + 1)]} trocou de ordem com a testemunha {nomes[troca]}")

# Printando nova lista
nomes_ordenados = ""
if len(nomes) > 0:
    for i in range(len(nomes)):
        nomes_ordenados += nomes[i] + " "
    nomes_ordenados = nomes_ordenados[:-1]
    print(nomes_ordenados)
