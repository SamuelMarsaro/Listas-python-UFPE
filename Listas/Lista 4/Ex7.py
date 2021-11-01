alfabeto = input()
alfabeto = alfabeto.split(" ")

comandos = input()
comandos = comandos.split()

ponto_inicial = input()
ponto_inicial = alfabeto.index(ponto_inicial)

string_completa = ""

for i in range(len(comandos)):
    try:
        # Comandos numericos:
        ultima_letra = alfabeto[ponto_inicial]
        x = int(comandos[i]) % 26
        ponto_inicial += x
        if ponto_inicial >= 26:
            ponto_inicial -= 26
        string_completa += alfabeto[ponto_inicial]
    except:
        # Espaços e letra repetida:
        if comandos[i] == "/":
            string_completa += " "
        elif comandos[i] == "R":
            string_completa += ultima_letra

print(string_completa)
