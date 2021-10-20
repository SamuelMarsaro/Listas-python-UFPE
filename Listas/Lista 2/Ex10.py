nome_da_musica = input()
novos_seguidores_michel = int(input())
novos_seguidores_raffa = int(input())
frase_1 = input()
frase_2 = input()
frase_3 = input()

seguidores_esperados = novos_seguidores_raffa + novos_seguidores_michel

if frase_1 == "Gang Gang Bro!":
    novos_seguidores_raffa = novos_seguidores_raffa * 1.25

elif frase_1 == "Hihiiiii UuHuu, 777 Bro!":
    novos_seguidores_raffa = novos_seguidores_raffa * 1.20
    novos_seguidores_michel = novos_seguidores_michel * 1.15

else:
    novos_seguidores_michel = novos_seguidores_michel * 0.70
    novos_seguidores_raffa = novos_seguidores_raffa * 0.75

if frase_2 == "Gang Gang Bro!":
    novos_seguidores_raffa = novos_seguidores_raffa * 1.25

elif frase_2 == "Hihiiiii UuHuu, 777 Bro!":
    novos_seguidores_raffa = novos_seguidores_raffa * 1.20
    novos_seguidores_michel = novos_seguidores_michel * 1.15

else:
    novos_seguidores_michel = novos_seguidores_michel * 0.70
    novos_seguidores_raffa = novos_seguidores_raffa * 0.75

if frase_3 == "Gang Gang Bro!":
    novos_seguidores_raffa = novos_seguidores_raffa * 1.25

elif frase_3 == "Hihiiiii UuHuu, 777 Bro!":
    novos_seguidores_raffa = novos_seguidores_raffa * 1.20
    novos_seguidores_michel = novos_seguidores_michel * 1.15

else:
    novos_seguidores_michel = novos_seguidores_michel * 0.70
    novos_seguidores_raffa = novos_seguidores_raffa * 0.75

seguidores_contatos = novos_seguidores_raffa + novos_seguidores_michel

resultado = (int(seguidores_contatos) / seguidores_esperados)*100


print("Então Michael, eu trouxe os seguintes resultados da música...")
print(f"Nome da Música: {nome_da_musica.upper()}")
print(f"Número de Seguidores Esperados: {seguidores_esperados}")
print(f"Número de Seguidores Calculados: {int(seguidores_contatos)}")
print(f"Resultado: {resultado:.2f}%")

if resultado >= 100:
    print("\nE felizmente... BROOO! faz sol! Camisa do Rusbé vai vender!")

elif resultado < 100:
    print("\nRockstar e fé em Deus bro! Que vocês irão pensar em frases melhores...")
