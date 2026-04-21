contador = 0
media = 0
acumulo = ""

while True:
    nota = float(input())
    if nota > 0 and nota <= 10.0:
        media += nota
        contador += 1
    elif nota < 0 or nota > 10.0:
        acumulo = acumulo + "nota invalida\n"
    if contador == 2:
            media = media / contador
            print(f"{acumulo}media = {media}")
            break
    