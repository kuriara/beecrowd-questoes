n = int(input())

x = input().split()

menor = int(x[0])
index = 0

for i in range(len(x)):
    if int(x[i]) < menor:
        menor = int(x[i])
        index = i

print(f"""Menor valor: {menor}
Posicao: {index}""")
