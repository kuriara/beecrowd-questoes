# renda = float(input())

# if renda <= 2000.00:
#     print("Isento")

# if renda > 4500.00:
#     renda_28 = (renda % 4500) * 28 / 100
#     renda_18 = (renda % 3000 - renda % 4500) * 18 / 100 
#     renda_8 = (renda % 2000 - renda % 3000) * 8 / 100
#     renda = renda_28 + renda_18 + renda_8
#     print(renda)

# elif renda > 3000.00 and renda <= 4500.00:
#     renda_18 = (renda % 3000) * 18 / 100
#     renda_8 = (renda % 2000 - renda % 3000) * 8 / 100
#     renda = renda_18 + renda_8
#     print(renda)

renda = float(input())

if renda <= 2000.00:
    print("Isento")

elif renda > 4500.00:
    renda_28 = (renda - 4500) * 28 / 100
    renda_18 = (renda - 3000 - (renda - 4500)) * 18 / 100
    renda_8 = (renda - 2000 - (renda - 3000)) * 8 / 100
    renda = renda_28 + renda_18 + renda_8
    print(f"R$ {renda:.2f}")

elif renda > 3000.00 and renda <= 4500.00:
    renda_18 = (renda - 3000) * 18 / 100
    renda_8 = (renda - 2000 - (renda - 3000)) * 8 / 100
    renda = renda_18 + renda_8
    print(f"R$ {renda:.2f}")

elif renda > 2000.00 and renda <= 3000.00:
    renda = (renda - 2000) * 8 / 100
    print(f"R$ {renda:.2f}")