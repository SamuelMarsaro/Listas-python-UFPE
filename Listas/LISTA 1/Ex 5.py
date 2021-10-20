# se 24000 ticks equivalem a 20 minutos 1 hora são 72000 ticks, contudo ele só usa 36000
d = int(input())
c = int(input())

ticks_per_house = d * 3 * 36000 / c
print(int(ticks_per_house))