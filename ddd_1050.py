ddd = int(input())
lista_ddd = [61, 71, 11, 21, 32, 19, 27, 31]

if ddd not in lista_ddd:
    print("DDD nao cadastrado")
else:
    if ddd == lista_ddd[0]:
        print("Brasilia")
    elif ddd == lista_ddd[1]:
        print("Salvador")
    elif ddd == lista_ddd[2]:
        print("Sao Paulo")
    elif ddd == lista_ddd[3]:
        print("Rio de Janeiro")
    elif ddd == lista_ddd[4]:
        print("Juiz de Fora")
    elif ddd == lista_ddd[5]:
        print("Campinas")
    elif ddd == lista_ddd[6]:
        print("Vitoria")
    elif ddd == lista_ddd[7]:
        print("Belo Horizonte")