i = 1
j = 8
contador = 0

while i <= 9:
    while contador < 3:
        j -= 1
        contador += 1
        print(f"I={i} J={j}")
    contador = 0
    i += 2
    j = 8