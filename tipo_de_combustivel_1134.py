def combustivel(codigo):
    alcool = gasolina = diesel = 0
    while True:
        if codigo == 1:
            alcool += 1
        elif codigo == 2:
            gasolina += 1
        elif codigo == 3:
            diesel += 1
        elif codigo == 4:
            return f"MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}"
        else:
            codigo = int(input())
        codigo = int(input())

def main():
    codigo = int(input())
    print(combustivel(codigo))

main()