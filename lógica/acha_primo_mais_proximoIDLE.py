def maior_primo(x):
    contaDivisoes = 3

    while contaDivisoes > 2:
        contaDivisoes = 0
        i = 1
       
        while i < x:
            if x % i == 0: #Se o número for divisível
                contaDivisoes += contaDivisoes 
        
            i += i #Incrementa I para testar a quantidade de divisões
            
    x -= 1

    if contaDivisoes < 3:
        return x

a = int(input("Número inteiro maior ou igual a 2: "))

maior_primo(a)
