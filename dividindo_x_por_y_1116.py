texto = ""

for i in range (2):
    n = int(input())
    if i == 0:
        n1 = n
    else:
        if n < n1:
            for i in range(n+1, n1):
                if i % 5 == 2 or i % 5 == 3:
                    texto = texto + f"{str(i)}\n"
        elif n1 < n:
            for i in range(n1+1, n):
                if i % 5 == 2 or i % 5 == 3:
                    texto = texto + f"{str(i)}\n"

print(texto, end="")
        