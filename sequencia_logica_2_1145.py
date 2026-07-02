x, y = input().split()
x, y = int(x), int(y)
contador = 0
numeros = 0

for i in range(y):
    contador += 1
    numeros += 1
    if contador == x:
        contador = 0
        print(f"{numeros}")
    else:
        print(f"{numeros} ", end="")
    if numeros == y:
        break

