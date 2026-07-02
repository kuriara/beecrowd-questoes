matriz = []

soma = 0
numero = 0
contador = 0

valor = int(input())
operacao = input()

for i in range(4):
    lista = []
    for j in range(4):
        numero = float(input())
        lista.append(numero)
    matriz.append(lista)


# [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == valor:
            soma = soma + matriz[i][j]
            contador += 1
            
if operacao == "S":
    numero = soma
if operacao == "M":
    numero = soma / contador
      


print(f"{numero:.1f}")