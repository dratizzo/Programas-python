#testa se há dígitos próximos iguais em um número

valorTot = int(input("Insira valor a ser testado: "))

nDivisao = 10
digitoTeste = 0
digitosIguais = False

while valorTot != 0 and not digitosIguais:
    x = valorTot % nDivisao #Isola o primeiro dígito
    
    digitoNovo = x #Guarda o primeiro digitado para ser testado

    if digitoNovo == digitoTeste:
            digitosIguais = True

    digitoTeste = x #Guarda o primeiro digitado para ser testado

    valorTot = valorTot // nDivisao #Remove o primeiro dígito para testar o próximo

if digitosIguais:
    print("Digitos adjacentes iguais.")
else:
    print("Não há dígitos adjacentes iguais.")




        
