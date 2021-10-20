nome1 = input()
nome2 = input()
nome3 = input()
nacionalidade1 = input()
nacionalidade2 = input()
nacionalidade3 = input()

numero_fases = int(input())

n, soma_notas1, soma_notas2, soma_notas3 = 0, 0, 0, 0

while n < numero_fases:
    nota1 = float(input())
    nota2 = float(input())
    nota3 = float(input())
    soma_notas1 += nota1
    soma_notas2 += nota2
    soma_notas3 += nota3
    n += 1

maior_nota = soma_notas1
maior_nacionalidade = nacionalidade1
maior_nome = nome1

if soma_notas2 > maior_nota:
    maior_nota = soma_notas2
    maior_nacionalidade = nacionalidade2
    maior_nome = nome2

if soma_notas3 > maior_nota:
    maior_nota = soma_notas3
    maior_nacionalidade = nacionalidade3
    maior_nome = nome3

if maior_nacionalidade == "Brasil":
    print(f"O vencedor da medalha de ouro de surf e {maior_nome}! E do Brasil!")
else:
    print(f"O vencedor da medalha de ouro de surf e {maior_nome}!")
