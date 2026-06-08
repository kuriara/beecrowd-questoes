matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma = contador = 0
operacao = input()

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i + j > len(matriz) - 1:
            soma = soma + matriz[i][j]
            contador += 1

if operacao == "S":
    print(soma)