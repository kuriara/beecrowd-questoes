contador = 1
positivo = 0
soma = 0

while contador <= 6:
    numero = float(input())
    if numero > 0.0:
        soma += numero
        positivo += 1
    contador += 1

media = soma / positivo

print(f"{positivo} valores positivos")
print(f"{media:.1f}")