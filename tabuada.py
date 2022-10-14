tabuada = int(input("Digite qual número você quer a tabuada: "))

print("Tabuada do número:", tabuada)

for valor in range(1, 11, 1):
    print(str(tabuada) + "x" + str(valor) + "=" + str(tabuada * valor))
