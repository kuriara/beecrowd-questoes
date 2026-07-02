while True:
    try:
        lista = []

        quantidade = int(input())

        velocidade = input().split()

        for i in velocidade:
            lista.append(int(i))

        lista_menor = []
        for i in range(quantidade):
            if lista[i] >= 20:
                lista_menor.append(3)
            elif lista[i] >= 10 and lista[i] < 20:
                lista_menor.append(2)
            elif lista[i] < 10:
                lista_menor.append(1)

        maior = lista_menor[0]

        for i in range(quantidade):
            if maior < lista_menor[i]:
                maior = lista_menor[i]

        print(maior)

    except EOFError:
        break