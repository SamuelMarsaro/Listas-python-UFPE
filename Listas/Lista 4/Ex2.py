SOBRENATURAIS = ['Damon Salvatore', 'Stefan Salvatore', 'Caroline Forbes', 'Elena Gilbert', 'Bonnie Bennett', 'Kai Parker', 'Katherine Pierce']
alvos = []

# Encontrando os sobrenaturais
try:
    while True:
        investigado = input()
        try:
            SOBRENATURAIS.index(investigado)
            if investigado not in alvos:
                alvos.append(investigado)
        except:
            alvos = alvos

# Printando os resultados
except:
    if len(alvos) == 0:
        print("Nenhum sobrenatural foi encontrado :/")
    else:
        print("Os sobrenaturais encontrados foram:\n")
        for i in range(len(alvos)):
            print(alvos[i])
        print("\nAgora Klaus, Rebekah, Elijah, Kol e toda a família original sabem bem em quem podem confiar e quem devem matar.")
