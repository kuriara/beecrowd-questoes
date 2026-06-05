t = int(input())

while t < 2 or t > 50:
    t = int(input("Digite um número válido - maior ou igual à 2 e menor ou igual à 50: "))

contador = 0
lista_vetor = []

while contador < 1000:
    for j in range(t):
        lista_vetor.append(j)
        contador += 1

contador_2 = 0

for i in range(1000+1):
    print(f"N[{contador_2}] = {lista_vetor[i]}")
    contador_2 += 1