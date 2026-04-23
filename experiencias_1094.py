n = int(input())
total_coelho = total_rato = total_sapo = 0

for i in range(n):
    coelho = rato = sapo = 0
    x, y = input().split()
    x = int(x)
    if y == "C":
        coelho += x
        total_coelho += coelho
    elif y == "R":
        rato += x
        total_rato += rato
    elif y == "S":
        sapo += x
        total_sapo += sapo

total = total_coelho + total_rato + total_sapo
porc_coelho = (total_coelho / total) * 100
porc_rato = (total_rato / total) * 100
porc_sapo = (total_sapo / total) * 100
porc_coelho = round(porc_coelho, 2)
porc_rato = round(porc_rato, 2)
porc_sapo = round(porc_sapo, 2)

print(f"Total: {total} cobaias\nTotal de coelhos: {total_coelho}\nTotal de ratos: {total_rato}\nTotal de sapos: {total_sapo}\nPercentual de coelhos: {porc_coelho} %\nPercentual de ratos: {porc_rato} %\nPercentual de sapos: {porc_sapo} %")
