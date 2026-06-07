n = int(input())
menor = 11

x = input().split(" ",n)


for i in range(len(x)):
    if int(x[i]) < menor:
        menor = int(x[i])
        index = i

print(f"""Menor valor: {menor}
Posicao: {index}""")
