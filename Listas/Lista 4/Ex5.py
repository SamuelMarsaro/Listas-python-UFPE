crimes = []
nomes = []
assassinos = []
ladroes = []
entrada = ["", ""]

# Recebendo e gerando as listas de crimes
while entrada[1] != "Doug Judy":
    entrada = input().split(": ")
    if entrada[1] != "Doug Judy":
        crimes.append(entrada[0])
        nomes.append(entrada[1])
        if entrada[0] == "Assassinato" and (entrada[1] not in assassinos):
            assassinos.append(entrada[1])

        elif (entrada[0] == "Roubo" or entrada[0] == "Furto") and (entrada[1] not in ladroes):
            ladroes.append(entrada[1])

# Recebendo o número de consultas
N = int(input())

# Ralizando as consultas
for i in range(N):
    operacao = input()
    if operacao == "1":
        criminoso = input()
        n_de_crimes_dele = nomes.count(criminoso)
        print(f"Na ficha de {criminoso} constam {n_de_crimes_dele} infrações este mês.")

    elif operacao == "2":
        crime = input()
        n_vezes_que_crime_ocorreu = crimes.count(crime)
        print(f"Neste mês foram cometidos {n_vezes_que_crime_ocorreu} {crime}")

    elif operacao == "3":
        print("Boletim de Ocorrências:")
        x = ""
        y = ""
        for j in range(len(assassinos)):
            x += assassinos[j] + ", "
        for j in range(len(ladroes)):
            y += ladroes[j] + ", "
        x = x[:-2]
        y = y[:-2]

        print(f"Assassinos: {x}")
        print(f"Ladroes: {y}")