pre_selecionadas = int(input())
capacidade_maxima_bunker = int(input())
capacidade_por_profissao = capacidade_maxima_bunker/4


# Recebendo todos pre-selecionados cabíveis
bunker = []
nomes = []
contador_engenheiros, contador_medicos, contador_prof, contador_cientista = 0, 0, 0, 0
pessoas_totais = 0
for i in range(pre_selecionadas):
    pessoa_perfil = input()
    pessoa_perfil = pessoa_perfil.split(": ")
    nomes.append(pessoa_perfil[0])

    if pessoa_perfil[1] == "Engenheiro(a)":
        if contador_engenheiros < capacidade_por_profissao:
            bunker.append(pessoa_perfil)
            contador_engenheiros += 1
            if contador_engenheiros == capacidade_por_profissao:
                print("Conseguimos chegar a quantidade maxima de Engenheiros")

    elif pessoa_perfil[1] == "Medico(a)":
        if contador_medicos < capacidade_por_profissao:
            bunker.append(pessoa_perfil)
            contador_medicos += 1
            if contador_medicos == capacidade_por_profissao:
                print("Conseguimos chegar a quantidade maxima de Medicos")

    elif pessoa_perfil[1] == "Cientista":
        if contador_cientista < capacidade_por_profissao:
            bunker.append(pessoa_perfil)
            contador_cientista += 1
            if contador_cientista == capacidade_por_profissao:
                print("Conseguimos chegar a quantidade maxima de Cientistas")

    elif pessoa_perfil[1] == "Professor(a)":
        if contador_prof < capacidade_por_profissao:
            bunker.append(pessoa_perfil)
            contador_prof += 1
            if contador_prof == capacidade_por_profissao:
                print("Conseguimos chegar a quantidade maxima de Professores")

    pessoas_totais = contador_prof + contador_cientista + contador_medicos + contador_engenheiros
    if pessoas_totais == capacidade_maxima_bunker:
        print("Chegamos a nossa capacidade maxima")
        print(
            f"\nRelatorio:\nMedicos: {contador_medicos}\nEngenheiros: {contador_engenheiros}\nCientistas: {contador_cientista}\nProfessores: {contador_prof}")
        break

# Algoritmo de seleção
x = 1

if pessoas_totais != capacidade_maxima_bunker:
    try:
        while x == 1:
            comando = input()
            if comando == "buscar":
                nome = input()
                try:
                    y = nomes.index(nome)
                    if y in range(len(nomes)):
                        print(f"{nome} ja esta no bunker")
                except:
                    print(f"{nome} ainda não chegou no bunker...")

            elif comando == "adicionar":
                adicionar = input()
                adicionar = adicionar.split(": ")
                nomes.append(adicionar[0])
                if adicionar[1] == "Engenheiro(a)":
                    if contador_engenheiros < capacidade_por_profissao:
                        bunker.append(adicionar)
                        contador_engenheiros += 1
                        if contador_engenheiros == capacidade_por_profissao:
                            print("Conseguimos chegar a quantidade maxima de Engenheiros")

                elif adicionar[1] == "Medico(a)":
                    if contador_medicos < capacidade_por_profissao:
                        bunker.append(adicionar)
                        contador_medicos += 1
                        if contador_medicos == capacidade_por_profissao:
                            print("Conseguimos chegar a quantidade maxima de Medicos")

                elif adicionar[1] == "Cientista":
                    if contador_cientista < capacidade_por_profissao:
                        bunker.append(adicionar)
                        contador_cientista += 1
                        if contador_cientista == capacidade_por_profissao:
                            print("Conseguimos chegar a quantidade maxima de Cientistas")

                elif adicionar[1] == "Professor(a)":
                    if contador_prof < capacidade_por_profissao:
                        bunker.append(adicionar)
                        contador_prof += 1
                        if contador_prof == capacidade_por_profissao:
                            print("Conseguimos chegar a quantidade maxima de Professores")
            else:
                print("**COMANDO INVALIDO**")
            pessoas_totais = contador_prof + contador_cientista + contador_medicos + contador_engenheiros
            if pessoas_totais == capacidade_maxima_bunker:
                print("Chegamos a nossa capacidade maxima")
                print(f"\nRelatorio:\nMedicos: {contador_medicos}\nEngenheiros: {contador_engenheiros}\nCientistas: {contador_cientista}\nProfessores: {contador_prof}")
                x += 1
    except:
        print(f"Na nossa busca no banco de dados, nao achamos pessoas suficientes com os parametros de selecao\n\nRelatorio:\nMedicos: {contador_medicos}\nEngenheiros: {contador_engenheiros}\nCientistas: {contador_cientista}\nProfessores: {contador_prof}")
