from math import sqrt

a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

delta = (b**2.0) - (4.0 * a * c)

if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    raizPositiva = ((-b) + sqrt(delta)) / (2.0 * a)
    raizNegativa = ((-b) - sqrt(delta)) / (2.0 * a)
    print(f"R1 = {raizPositiva:.5f}\nR2 = {raizNegativa:.5f}")

