numero = int(input())
contador = 1

lista = ["tesoura", "papel", "pedra", "lagarto", "Spock", "tesoura", "lagarto", "papel", "Spock", "pedra"]
lista_2 = ["papel", "pedra", "lagarto", "Spock", "tesoura", "lagarto", "papel", "Spock", "pedra", "tesoura"]

while contador <= numero:

    x, y = input().split()

    if x == y:
        print(f"Caso #{contador}: De novo!")

    for i in range(len(lista)):
        if lista[i] == x and lista_2[i] == y:
            print(f"Caso #{contador}: Bazinga")
        elif lista[i] == y and lista_2[i] == x:
            print(f"Caso #{contador}: Raj trapaceou")

    contador += 1
