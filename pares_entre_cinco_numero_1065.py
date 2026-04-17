contador = 1
positivo = 0

while contador <= 5:
    numero = int(input())
    if numero % 2 == 0:
        positivo += 1
    contador += 1

print(f"{positivo} valores pares")