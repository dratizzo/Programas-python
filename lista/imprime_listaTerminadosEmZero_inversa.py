    
x = int(input("Valores terminados em 0: "))
i = -1
lis = []

while x != 0:   
    if x % 10 == 0:
        lis.append(x)
    else:
        print("Digite um valor válido!!!")
        
    x = int(input("Valores terminados em 0: "))

tam = len(lis) * -1
while i != tam - 1:
    print(lis[i])
    i = i - 1
