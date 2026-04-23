senha = 2002
texto = ""
numero = int(input())

while numero != senha:
    numero = int(input())
    texto = texto + "Senha Invalida\n"
else:
    texto = texto + "Acesso Permitido"

print(texto)
