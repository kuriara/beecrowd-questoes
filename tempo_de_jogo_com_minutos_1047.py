horas_iniciais, minutos_iniciais, horas_finais, minutos_finais = input().split()

horas_iniciais, minutos_iniciais, horas_finais, minutos_finais = int(horas_iniciais), int(minutos_iniciais), int(horas_finais), int(minutos_finais)

horas = horas_finais - horas_iniciais

minutos = minutos_finais - minutos_iniciais

if minutos < 0:
    minutos = 60 + minutos
    horas = horas - 1

if horas < 0:
    horas = 24 + horas

if minutos == 0 and horas == 0:
    minutos == horas == 24

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")