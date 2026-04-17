contador = 1
par = 0
impar = 0
positivo = 0
negativo = 0

while contador <= 5:
    numero = int(input())
    if numero % 2 == 0:
        par += 1
    elif numero % 2 != 0:
        impar += 1
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1
    contador += 1

print(f"{par} valor(es) par(es)\n{impar} valor(es) impar(es)\n{positivo} valor(es) positivo(s)\n{negativo} valor(es) negativo(s)")