matriz = []

contador = 0
soma = 0
operacao = input()

for i in range(3):
    lista = []
    for j in range(3):
        numero = int(input())
        lista.append(numero)
    matriz.append(lista)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i + j < (len(matriz) - 1) and j > i:
            soma = soma + matriz[i][j]
            contador += 1

if operacao == "S":
    print(soma)

if operacao == "M":
    print(soma / contador)
        