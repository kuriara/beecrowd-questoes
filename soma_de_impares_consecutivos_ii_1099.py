valor = int(input())
contador = 1
soma_impares = 0
cadeia = ""

while contador <= valor:
    x, y = input().split()
    x, y = int(x), int(y)
    soma_impares = 0
    if x == y:
        cadeia = cadeia + "\n" + "0" 
    elif y > x:
        if x % 2 == 1 and soma_impares == 0:
            x += 1
        while x < y:
            if x % 2 == 1:
                soma_impares += x
                soma_impares_string = str(soma_impares)
            x += 1
        if soma_impares == 0:
            cadeia = cadeia + "\n" + "0" 
        else:
            cadeia = cadeia + "\n" + soma_impares_string
    elif x > y:
        if y % 2 == 1 and soma_impares == 0:
            y += 1
        while y < x:
            if y % 2 == 1:
                soma_impares += y
                soma_impares_string = str(soma_impares)
            y += 1
        if soma_impares == 0:
            cadeia = cadeia + "\n" + "0" 
        else:
            cadeia = cadeia +  "\n" + soma_impares_string 
    contador += 1

cadeia = cadeia.lstrip()
print(cadeia)