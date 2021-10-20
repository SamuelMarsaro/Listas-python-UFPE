genero = input()
nacional = input()
decada = input()

if genero == "Rock" and nacional == "Nao" and decada == "70":
    print("A musica que voce esta procurando eh: Bohemian Rapsody")
elif genero == "Samba" and nacional == "Sim" and decada == "80":
    print("A musica que voce esta procurando eh: Conselho")
elif genero == "Samba" and nacional == "Sim" and decada == "70":
    print("A musica que voce esta procurando eh: Apesar de Voce")
elif genero == "Pop" and nacional == "Nao" and decada == "90":
    print("A musica que voce esta procurando eh: Candle in the Wind 1997")
elif genero == "Samba" and nacional == "Sim" and decada == "60":
    print("A musica que voce esta procurando eh: Mas que nada")
elif genero == "Rock" and nacional == "Sim" and decada == "80":
    print("A musica que voce esta procurando eh: Indios")
elif genero == "Pop" and nacional == "Nao" and decada == "80":
    print("A musica que voce esta procurando eh: Take On Me")
elif genero == "Pop" and nacional == "Sim" and decada == "90":
    print("A musica que voce esta procurando eh: Anna Julia")
elif genero == "Rock" and nacional == "Sim" and decada == "70":
    print("A musica que voce esta procurando eh: O Pirata")
else:
    print("Musica nao encontrada")