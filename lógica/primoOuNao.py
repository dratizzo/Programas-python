def primo(n):
    fator = 2
    if n == 2:
        return True
    
    while n % fator != 0 and fator < n/2:
        fator += 1
    if n % fator == 0:
        return False
    else:
        return True

n = int(input("Número inteiro positivo: "))

while n >= 0:
    if primo(n):
        print("primo")
    else:
        print("não primo")
    n = int(input("Número inteiro positivo: "))

