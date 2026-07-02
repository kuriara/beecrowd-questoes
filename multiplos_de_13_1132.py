x = int(input())
y = int(input())
soma = 0

if x > y:
    novo = y
    y = x
    x = novo
    
for i in range (x, y + 1):
    if i % 13 != 0:
        soma += i

print(soma)