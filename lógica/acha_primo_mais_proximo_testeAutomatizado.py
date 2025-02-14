def maior_primo(x):
    contaDivisoes = 3

    while contaDivisoes > 2:
        contaDivisoes = 0
        i = 1
       
        while i < x:
            if x % i == 0: #Se o número for divisível
                contaDivisoes += 1
        
            i += 1 #Incrementa I para testar a quantidade de divisões
            
        if contaDivisoes > 2:
            x -= 1

    if contaDivisoes < 3:
        return x

#a = int(input("Número inteiro maior ou igual a 2: "))

#print(maior_primo(a))

def test_maior_primo():
    if maior_primo(15) == 13:
        print("Funciona para 15")
    else:
        print("Não funciona para 15")
    if maior_primo(7) == 7:
        print("Funciona para 7")
    else:
        print("Não funciona para 7")
        
