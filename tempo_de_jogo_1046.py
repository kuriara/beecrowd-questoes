a, b = input().split()

a = int(a)
b = int(b)

if a >= b:
    tempo = 24 - (a - b)
    if tempo >= 1 and tempo <= 24:
        print(f"O JOGO DUROU {tempo} HORA(S)")
elif b > a:
    tempo = b - a
    if tempo >= 1 and tempo <= 24:
        print(f"O JOGO DUROU {tempo} HORA(S)")