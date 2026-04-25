x, y = input().split()
x, y = int(x), int(y)

if y < 0:
    y = -(y)
    quociente = x // y
    quociente = -(quociente)
    resto = x % y
    print(f"{quociente} {resto}")
elif x < 0:
    quociente = x // y
    resto = x % y
    print(f"{quociente} {resto}")
else:
    quociente = x // y
    resto = x % y
    print(f"{quociente} {resto}")