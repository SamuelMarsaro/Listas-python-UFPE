QNT_OBSTACULOS = 10
voltas = int(input())
contador_erro, contador_erro_seguido, contador_voltas = 0, 0, 1
tempo_limite = 72
anterior = ""
obstaculo_total = voltas * QNT_OBSTACULOS
for i in range(obstaculo_total):
    erro_acerto = input()
    if contador_voltas % 10 == 0:
        tempo_limite = 72
        contador_erro_seguido = 0
    if erro_acerto == "erro" and anterior == "erro":
        contador_erro_seguido += 1
        if contador_erro_seguido == 1 or contador_erro_seguido == 3:
            print("Voce precisa melhorar, Carlinhos")
        if contador_erro_seguido == 4:
            print("O treino de hoje nao esta rendendo Carlinhos, vamos tentar de novo amanha")
            break
    if erro_acerto == "acerto":
        contador_erro_seguido = 0
        tempo_limite -= 5
        if tempo_limite <= 0:
            print("Temos que trabalhar urgentemente na sua velocidade, voce precisa errar menos")
            break
    elif erro_acerto == "erro":
        contador_erro += 1
        tempo_limite -= 9
        if tempo_limite <= 0:
            print("Temos que trabalhar urgentemente na sua velocidade, voce precisa errar menos")
            break
    anterior = erro_acerto
    contador_voltas += 1

if contador_erro == 0 and tempo_limite > 0:
    print("Que desempenho excelente, Carlinhos, melhor impossivel")
elif contador_erro > 0:
    print("Seu desempenho esta bom, mas poderia ter sido muito melhor")
