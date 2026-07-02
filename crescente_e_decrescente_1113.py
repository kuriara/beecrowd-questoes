texto = ""

while True:
    x, y = input().split()
    x, y = int(x), int(y)

    if x > y:
        texto = texto + "Decrescente\n"
    if x < y:
        texto = texto + "Crescente\n"
    if x == y:
        break

print(texto, end="")