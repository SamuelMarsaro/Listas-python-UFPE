diferenca_pontos = 0
pontos_federer = 0
pontos_djoko = 0
while (pontos_djoko < 4 and pontos_federer < 4) or (pontos_djoko >=4 and diferenca_pontos < 2) or (pontos_federer >= 4 and diferenca_pontos < 2):
    rodada = input()
    if rodada == "federer":
        pontos_federer += 1
        diferenca_pontos = pontos_federer - pontos_djoko
    if rodada == "djoko":
        pontos_djoko += 1
        diferenca_pontos = pontos_djoko - pontos_federer

if pontos_djoko > pontos_federer:
    print(f"Djokovic ganhou o game com a pontuacao de {pontos_djoko} a {pontos_federer}!")
else:
    print(f"Roger federer ganhou o game com a pontuacao de {pontos_federer} a {pontos_djoko}!")