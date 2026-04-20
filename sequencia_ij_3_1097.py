i = 1
j = i + 6
contador = 1

while i <= 9:
    while contador <= 3:
        print(f"I={i} J={j}")
        contador += 1
        j -= 1
    i += 2
    j = i + 6
    contador = 1