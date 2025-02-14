
'''

Escreva uma função que recebe um array de
strings como parâmetro e devolve o primeiro string
na ordem lexicográfica, ignorando-se letras maiúsculas
e minúsculas.
'''

def menor_string(meu_string):
    stringMaisCurta = "z"
    
    for i in range(0, len(meu_string)):
        limpa_string = meu_string[i].lower().strip()
        
        if stringMaisCurta > limpa_string:
            stringMaisCurta = limpa_string

    return stringMaisCurta

def testa_menor_string():
    teste_pontual = ["ana", "maria", "José", "Valdemar"]
    if (menor_string(teste_pontual) == "ana"):
        print("Correto para 'ana'.")
    else:
        print("Errado para 'ana'.")
    
    teste_pontual = [ "Thiago", "marta", "Ricardo", "gustavo"]
    if (menor_string(teste_pontual) == "gustavo"):
        print("Correto para 'gustavo'.")
    else:
        print("Errado para 'gustavo'.")
        
    teste_pontual = ["Juliana", "lucas", "Rafaela", "felipe"]
    if (menor_string(teste_pontual) == "felipe"):
        print("Correto para 'felipe'.")
    else:
        print("Errado para 'felipe'.")

    teste_pontual = ["joão", "carlos", "mariana", "gabriel", "Sofia"]
    if (menor_string(teste_pontual) == "carlos"):
        print("Correto para 'carlos'.")
    else:
        print("Errado para 'carlos'.")
    