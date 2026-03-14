a, b, c, d = input().split()

a = float(a)
b = float(b)
c = float(c)
d = float(d)

media = (a * 2 + b * 3 + c * 4 + d * 1) / 10

print(f"Media: {media:.1f}")

if media < 5.0:
    print("Aluno reprovado.")
elif media >= 5.0 and media < 7.0:
    print("Aluno em exame.")
    exame = float(input())
    print(f"Nota do exame: {exame:.1f}")
    nova_media = (exame + media) / 2
    if nova_media > 5.0:
        print("Aluno aprovado.")
    elif nova_media < 5.0:
        print("Aluno reprovado.")
    print(f"Media final: {nova_media:.1f}")
elif media >= 7.0:
    print("Aluno aprovado.")