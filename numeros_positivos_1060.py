contador = 0

numero1 = int(input())
numero2 = int(input())
numero3 = int(input())
numero4 = int(input())
numero5 = int(input())
numero6 = int(input())

lista = [numero1, numero2, numero3, numero4, numero5, numero6]

if numero1 > 0:
    contador +=1
if numero2 > 0:
    contador +=1
if numero3 > 0:
    contador +=1
if numero4 > 0:
    contador +=1
if numero5 > 0:
    contador +=1
if numero6 > 0:
    contador +=1

print(f"{contador} valores positivos")
