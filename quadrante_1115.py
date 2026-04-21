quadrante = ""

while True:
    x, y = input().split()
    x, y = int(x), int(y)
    if x > 0 and y > 0:
        quadrante = quadrante + "primeiro\n"
    elif x > 0 and y < 0:
        quadrante = quadrante + "quarto\n"
    elif x < 0 and y < 0:
        quadrante = quadrante + "terceiro\n"
    elif x < 0 and y > 0:
        quadrante = quadrante + "segundo\n"
    elif x == 0 or y == 0:
        break

quadrante = quadrante.lstrip()

print(quadrante, end="")