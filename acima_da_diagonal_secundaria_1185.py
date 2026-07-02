matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma = contador = 0
operacao = input()

for i in range(12):
    lista = []
    for j in range(12):
        numero = float(input())
        lista.append(numero)
    matriz.append(lista)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if len(matriz) - 1 > i + j:
            soma = soma + matriz[i][j]
            contador += 1

if operacao == "S":
    print(soma)
if operacao == "M":
    print(f"{soma / contador:.1f}")