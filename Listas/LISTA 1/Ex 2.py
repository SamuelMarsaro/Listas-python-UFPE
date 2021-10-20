hogsmade = {"X": 34, "Y": 110, "Z": 220}
kakariko = {"X": 0, "Y": 64, "Z": 0}
solitude = {"X": 140, "Y": 200, "Z": 456}

position_x = int(input())
position_z = int(input())
d_hogsmade = ((hogsmade["X"] - position_x)**2 + (hogsmade["Z"] - position_z)**2)**0.5
d_kakariko = ((kakariko["X"] - position_x)**2 + (kakariko["Z"] - position_z)**2)**0.5
d_solitude = ((solitude["X"] - position_x)**2 + (solitude["Z"] - position_z)**2)**0.5

print("Distancia para Hogsmeade:", "{:.2f}".format(d_hogsmade))
print("Distancia para Kakariko:", "{:.2f}".format(d_kakariko))
print("Distancia para Solitude:", "{:.2f}".format(d_solitude))
