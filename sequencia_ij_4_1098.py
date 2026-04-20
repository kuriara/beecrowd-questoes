i = 0
j = 0
contador = 1

while i <= 2:
    while contador <= 3:
        j += 1
        valor = j + i
        if i == int(i):
            print(f"I={i:.0f} J={valor:.0f}")
        else:
            print(f"I={i} J={valor}")
        contador += 1
    j = 0
    i += 0.2
    i = round(i, 1)
    contador = 1