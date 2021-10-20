objeto_1 = input()
objeto_2 = input()
objeto_3 = input()
objeto_4 = input()
objetos_encontrados = 0

if objeto_1 == "Alicate" or objeto_1 == "Chave de Fenda" or objeto_1 == "Lanterna" or objeto_1 == "Martelo":
    objetos_encontrados += 1
if objeto_2 == "Alicate" or objeto_2 == "Chave de Fenda" or objeto_2 == "Lanterna" or objeto_2 == "Martelo":
    objetos_encontrados += 1
if objeto_3 == "Alicate" or objeto_3 == "Chave de Fenda" or objeto_3 == "Lanterna" or objeto_3 == "Martelo":
    objetos_encontrados += 1
if objeto_4 == "Alicate" or objeto_4 == "Chave de Fenda" or objeto_4 == "Lanterna" or objeto_4 == "Martelo":
    objetos_encontrados += 1

if objetos_encontrados == 4:
    print("Tuê, encontrei tudo! Tá tudo Jóia, ficou bem BOOMZIM!!!")
elif objetos_encontrados == 0:
    print("Tuêzin! Se a seca chegar, não vai se desanimar...")
else:
    print("Andam dizendo que o Tuê é um baiano...")