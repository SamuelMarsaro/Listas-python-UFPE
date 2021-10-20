vida_logan = 100
vida_eu = 100
n = 1

while vida_eu > 0 and vida_logan > 0:
    if n % 2 == 0:
        ataque = int(input())
        defesa = int(input())
        diferenca = ataque - defesa
        if 0 < diferenca <= 20:
            vida_logan -= diferenca
        elif diferenca > 20:
            vida_logan -= 1.5 * diferenca
        elif diferenca < -20:
            vida_eu -= diferenca * -1
    else:
        ataque = int(input())
        defesa = int(input())
        diferenca = ataque - defesa
        if 0 < diferenca <= 20:
            vida_eu -= diferenca
        elif diferenca > 20:
            vida_eu -= 1.5 * diferenca
        elif diferenca < -20:
            vida_logan += diferenca
    n += 1
else:
    if vida_logan <= 0:
        print("Apos longos anos de esforco voce finalmente conseguiu, e ouro pro Brasil!")
    elif vida_eu <= 0:
        print("Infelizmente nao foi dessa vez, Logan Paul leva a vitoria.")
