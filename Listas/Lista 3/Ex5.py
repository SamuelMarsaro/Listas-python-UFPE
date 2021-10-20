energia1 = int(input())
peso1 = int(input())
energia2 = int(input())
peso2 = int(input())
energia3 = int(input())
peso3 = int(input())

i, j, k = 0, 0, 0
n = 0

while n < 3:
    peso_levantar1 = int(input())
    if energia1 > 0:
        diferenca1 = peso_levantar1 / peso1
        energia1 -= diferenca1
    if energia1 <= 0:
        if i == 0:
            print("O competidor 1, desmaiou")
            i += 1

    peso_levantar2 = int(input())
    if energia2 > 0:
        diferenca2 = peso_levantar2 / peso2
        energia2 -= diferenca2
    if energia2 <= 0:
        if j == 0:
            print("O competidor 2, desmaiou")
            j += 1

    peso_levantar3 = int(input())
    if energia3 > 0:
        diferenca3 = peso_levantar3 / peso3
        energia3 -= diferenca3
    if energia3 <= 0:
        if k == 0:
            print("O competidor 3, desmaiou")
            k += 1

    n += 1
desmaios = i + j + k

melhor_energia = 1000000

if 0 < energia1 < melhor_energia:
    melhor_energia = energia1
    competidor_vencedor = 1

if 0 < energia2 < melhor_energia:
    melhor_energia = energia2
    competidor_vencedor = 2

if 0 < energia3 < melhor_energia:
    melhor_energia = energia3
    competidor_vencedor = 3

if desmaios == 3:
    print("Todos os competidores desmaiaram")
else:
    print(f"O vencedor foi o competidor {competidor_vencedor}")
