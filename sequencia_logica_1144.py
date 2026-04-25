n = int(input())

for i in range(1, n+1):
    contador = 1
    while contador < 2:
        print(f"{i} {i**2} {i**3}")
        contador += 1
        if contador == 2:
            print(f"{i} {(i**2)+1} {(i**3)+1}")