print("Determina se um numero n eh triangular\n")

num = int(input("Valor: "))

produto = x = 0

while produto <= num:
    produto = (x + 1) * (x + 2) * (x + 3)
    if produto == num:
        condicao = True
        #print("Triangular")
        break
    else:
        if  produto != num:
            condicao = False
            #print("Não é triangular")

    x += 1

if condicao:
    print("Triangular")

else:
    print("Não é triangular")
