nome = input()
jogos = int(input())
n = 0

while n < jogos:
    numero_gols = int(input())
    if n == 0:
        menor_gols = numero_gols
        maior_gols = numero_gols
    elif numero_gols < menor_gols:
        menor_gols = numero_gols
    elif numero_gols > maior_gols:
        maior_gols = numero_gols
    n += 1

print(f"Belo dia de treinos, {nome}! Hoje o seu melhor desempenho foi de {maior_gols} gols e o pior foi de {menor_gols} gols. Rumo ao Ouro!")