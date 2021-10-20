frase_1 = input()
frase_2 = input()
frase_3 = input()
frase_4 = input()

pontuacao = 0

if frase_1 == "Sua apresentacao foi incrivel!":
    pontuacao += 200
elif frase_1 == "Voce errou algumas notas, mas tem potencial":
    pontuacao += pontuacao**0.5
elif frase_1 == "Sua performance me deu dor de cabeca!":
    if pontuacao > 100:
        pontuacao = pontuacao - 100
    elif pontuacao <= 100:
        pontuacao = 0

if frase_2 == "Sua apresentacao foi incrivel!":
    pontuacao += 200
elif frase_2 == "Voce errou algumas notas, mas tem potencial":
    pontuacao += pontuacao**0.5
elif frase_2 == "Sua performance me deu dor de cabeca!":
    if pontuacao > 100:
        pontuacao = pontuacao - 100
    elif pontuacao <= 100:
        pontuacao = 0

if frase_3 == "Sua apresentacao foi incrivel!":
    pontuacao += 200
elif frase_3 == "Voce errou algumas notas, mas tem potencial":
    pontuacao += pontuacao**0.5
elif frase_3 == "Sua performance me deu dor de cabeca!":
    if pontuacao > 100:
        pontuacao = pontuacao - 100
    elif pontuacao <= 100:
        pontuacao = 0

if frase_4 == "Sua apresentacao foi incrivel!":
    pontuacao += 200
elif frase_4 == "Voce errou algumas notas, mas tem potencial":
    pontuacao += pontuacao**0.5
elif frase_4 == "Sua performance me deu dor de cabeca!":
    if pontuacao > 100:
        pontuacao = pontuacao - 100
    elif pontuacao <= 100:
        pontuacao = 0

if pontuacao > 150:
    print(f"Parabens! Voce atingiu a pontuacao de {pontuacao:.2f} e passou para a proxima fase!")
elif pontuacao >= 100:
    print("Foi por pouco! Voce tem que ajustar algumas notas para alcancar a pontuacao necessaria")
else:
    print("A area musical nao foi feita para voce!")
