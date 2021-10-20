genero = int(input())
if genero == 1:
    print("Você escolheu o gênero: Rock")
elif genero == 2:
    print("Você escolheu o gênero: Eletronica")
else:
    print("Você escolheu o gênero: Hip-hop/Rap")

print("Escolha a musica")
musica = int(input())

if genero == 1:
    if musica == 1:
        print("Tocando: In the end - Linkin Park")
    elif musica == 2:
        print("Tocando: Californication - Red Hot Chilli Peppers")
    else:
        print("Tocando: Yellow - Coldplay")

elif genero == 2:
    if musica == 1:
        print("Tocando: Big Jet Plane - Alok & Mathieu")
    elif musica == 2:
        print("Tocando: Everyday - Marshmello & Logic")
    else:
        print("Tocando: On & On - Cartoon")

else:
    if musica == 1:
        print("Tocando: Congratulations - Post Malone")
    elif musica == 2:
        print("Tocando: HIGHEST IN THE ROOM - Travis Scott")
    else:
        print("Tocando: Devil Eyes - Hippie Sabotage")