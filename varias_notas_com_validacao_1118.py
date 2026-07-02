contador = 0
texto = ""

while True:
    n = float(input())
    if contador == 1 and n >= 0.0 and n <= 10.0:
        media = (n + n2) / 2
        texto = f"{texto}media = {media:.2f}\n"
        pergunta = int(input())
        while pergunta != 1 and pergunta != 2:
            texto = texto + "novo calculo (1-sim 2-nao)\n"
            pergunta = int(input())
        if pergunta == 1:
            texto = texto + "novo calculo (1-sim 2-nao)\n"
            contador = 0
            continue
        elif pergunta == 2:
            texto = texto + "novo calculo (1-sim 2-nao)\n"
            print(texto, end="")
            break
    if n >= 0.0 and n <= 10.0:
        n2 = n
        contador += 1
    else:
        texto = texto + "nota invalida\n"

