texto = "Novo grenal (1-sim 2-nao)\n"
soma_inter = soma_gremio = empate = 0
contador = 1
x, y = input().split()
x, y = int(x), int(y)
if x > y:
    soma_inter += 1
if x < y:
    soma_gremio += 1
if x == y:
    empate += 1

while True:
    grenal = int(input())
    if grenal == 1:
        x, y = input().split()
        x, y = int(x), int(y)
        texto = texto + "Novo grenal (1-sim 2-nao)\n"
        contador += 1
        if x > y:
            soma_inter += 1
        if x < y:
            soma_gremio += 1
        if x == y:
            empate += 1
        x = y = 0 
    if grenal == 2:
        print(texto,end="")
        print(f"{contador} grenais")
        print(f"Inter:{soma_inter}\nGremio:{soma_gremio}\nEmpates:{empate}")
        if soma_inter > soma_gremio:
            print("Inter venceu mais")
        elif soma_inter < soma_gremio:
            print("Gremio venceu mais")
        else:
            print("Nao houve vencedor")
        break
