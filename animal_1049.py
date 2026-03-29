esqueleto = input()
tipo = input()
alimentacao = input()

if esqueleto == "vertebrado":
    if tipo == "ave":
        if alimentacao == "carnivoro":
            print("aguia")
        if alimentacao == "onivoro":
            print("pomba")
    if tipo == "mamifero":
        if alimentacao == "onivoro":
            print("homem")
        if alimentacao == "herbivoro":
            print("vaca")
if esqueleto == "invertebrado":
    if tipo == "inseto":
        if alimentacao == "hematofago":
            print("pulga")
        if alimentacao == "herbivoro":
            print("herbivoro")
    if tipo == "anelideo":
        if alimentacao == "hematofago":
            print("sanguessuga")
        if alimentacao == "onivoro":
            print("minhoca")

# elif esqueleto == "invertebrado":

# else:
#     print("ERRO")