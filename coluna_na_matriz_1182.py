matriz = []

contador = 0
soma = 0
numero = 0

quantidade = int(input())
operacao = input()

for i in range(3):
    lista = []
    for j in range(3):
        numero = float(input())
        lista.append(numero)
    matriz.append(lista)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j == quantidade:
            soma = soma + matriz[i][j]
            numero = soma
            contador += 1

if operacao == "S":
    print(f"{soma:.1f}")

if operacao == "M":
    print(f"{soma / contador:.1f}")



