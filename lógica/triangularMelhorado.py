print("Determina se um numero n eh triangular\n")

num = int(input("Valor: "))

x = 1

while x * (x + 1) * (x + 2) < num:
    x += 1
    
    if x * (x + 1) * (x + 2) == num:
        print("Triangular")
    else:
        print("Não é triangular")
        
