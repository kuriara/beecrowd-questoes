par = []
impar = []
contador_par = contador_impar = 0



for i in range(5):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
        if len(par) == 2:
            for j in range(2):
                print(f"par[{j}] = {par[j]}")
            par = []
    if n % 2 == 1:
        impar.append(n)
        if len(impar) == 2:
            for j in range(2):
                print(f"impar[{j}] = {impar[j]}")
            impar = []

if impar:
    for i in range(len(impar)):
        print(f"impar[{i}] = {impar[i]}")

if par:
    for i in range(len(par)):
        print(f"par[{i}] = {par[i]}")