a, b = input().split()

a = int(a)
b = int(b)

contador = float(0)

if a == 1:
    contador = b * 4.00
if a == 2:
    contador = b * 4.50
if a == 3:
    contador = b * 5.00
if a == 4:
    contador = b * 2.00
if a == 5:
    contador = b * 1.50

print(f"Total: R$ {contador:.2f}")