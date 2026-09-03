contador = 0
valor = 0
nome = input()


while contador != 3:
    if nome != "caw caw":
        nome = nome[::-1]
        for i in range(len(nome)):
            if nome[i] == "*":
                valor = valor + 2 ** i
    if nome == "caw caw":
        contador += 1
        print(valor)
        valor = 0
        if contador == 3:
            break
    nome = input()
    