# n = int(input())
# contador = 2
# mensagem = ""

# while contador <= n:
#     if contador % 2 == 0:
#         valor = contador ** 2
#         somatorio = f"{contador}^2 = {valor}\n"
#         mensagem = mensagem + somatorio
#     contador+=1
# print(mensagem, end="")

n = int(input())

for i in range(1, n+1):
    if i % 2 == 0:
        valor = i ** 2
        somatorio = f"{i}^2 = {valor}"
        print(somatorio)
