salario = float(input())

if salario >= 0 and salario <= 400.00:
    reajuste = salario * 15/100
    novo_salario = salario + reajuste
    print(f"Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 15 %")

elif salario > 400.00 and salario <= 800.00:
    reajuste = salario * 12/100
    novo_salario = salario + reajuste
    print(f"Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 12 %")

elif salario > 800.00 and salario <= 1200.00:
    reajuste = salario * 10/100
    novo_salario = salario + reajuste
    print(f"Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 10 %")

elif salario > 1200.00 and salario <= 2000.00:
    reajuste = salario * 7/100
    novo_salario = salario + reajuste
    print(f"Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 7 %")

elif salario > 2000.00:
    reajuste = salario * 4/100
    novo_salario = salario + reajuste
    print(f"Novo salario: {novo_salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: 4 %")