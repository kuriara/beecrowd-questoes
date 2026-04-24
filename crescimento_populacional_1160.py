t = int(input())

for i in range(t):
    x, y, a, b = input().split()
    x, y = int(x), int(y)
    a, b = float(a), float(b)
    parcela = 0
    contador = 0
    while x <= y:
        parcela = (x * (a/100))
        parcela = int(parcela)
        parcela2 = (y * (b/100))
        parcela2 = int(parcela2)
        x = x + parcela
        y = y + parcela2
        contador += 1
        if contador > 100:
            print("Mais de 1 seculo.")
            break
        elif contador <= 100 and x > y:
            print(f"{contador} anos.")
            break
    
        
    
        
    

# while media != media2:
#     parcela = (media * 0.01)
#     parcela = int(parcela)
#     media = media + parcela
#     contador += 1
#     if media == media2:
#         break

# print(contador)