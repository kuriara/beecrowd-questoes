n = int(input())
texto = ""

for i in range(n):
    x, y = input().split()
    x, y = float(x), float(y)
    try:
        divisao = x / y
    except ZeroDivisionError:
        texto = texto + "divisao impossivel\n"
    else:
        texto = f"{texto}{divisao:.1f}\n"

print(texto, end="")
        