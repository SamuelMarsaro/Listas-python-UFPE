numero = ""
numeros_ordenados = list()

while numero != "fim":
    numero = input()
    if numero != "fim":
        numeros_ordenados.append(int(numero))

for i in range(len(numeros_ordenados)):
    for j in range(len(numeros_ordenados)):
        if numeros_ordenados[i] <= numeros_ordenados[j]:
            k = numeros_ordenados[j]
            numeros_ordenados[j] = numeros_ordenados[i]
            numeros_ordenados[i] = k

for i in range(len(numeros_ordenados)):
    print(numeros_ordenados[i])
