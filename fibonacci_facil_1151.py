n = int(input())

x = 1
y = 1
z = 0
contador = 0
while contador < n:
    contador += 1
    if contador < 3:
        print(f"{x-y}", end="" if contador == n else " ")
        if contador == 2:
            continue
        z = x + y
        x = z
    if contador >= 3:
        w = x
        z = x + y
        x = z
        y = w
        h = x - y
        print(f"{h}", end="" if contador == n else " ")

print()
            
