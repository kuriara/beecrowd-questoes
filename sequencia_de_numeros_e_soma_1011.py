soma_str = ""
soma_string = ""

while True:
    m, n = input().split()
    m, n = int(m), int(n)
    soma = 0
    if m > 0 and n > 0:
            if m < n:
                soma_str = str(m)
                soma = m
                while m <= n:
                    if m == n:
                        soma_string = soma_string + soma_str + f" Sum={soma}\n" 
                        break
                    else:
                        soma_string = soma_string + soma_str + " "
                        m = m + 1
                        soma += m
                        soma_str = str(m)
            elif n < m:
                soma_str = str(n)
                soma = n
                while n <= m:
                    if m == n:
                        soma_string = soma_string + soma_str + f" Sum={soma}\n" 
                        break
                    else:
                        soma_string = soma_string + soma_str + " "
                        n = n + 1
                        soma += n
                        soma_str = str(n)
    else:
        break
print(soma_string, end="")

            
        

