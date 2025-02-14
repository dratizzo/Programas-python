def menor_string(meu_string):
    stringMaisCurta = meu_string[0]
    
    for i in meu_string:
        i = i.lower().strip()
        
        if stringMaisCurta > i:
            stringMaisCurta = i

    return stringMaisCurta
    
teste_pontual = ["Juliana", "CARLOS", "lucas", "Rafaela", "felipe"]
print(menor_string(teste_pontual))

def testa_menor_string():
    teste_pontual = ["ana", "maria", "José", "Valdemar"]
    if (menor_string(teste_pontual) == "ana"):
        print("Correto para 'ana'.")
    else:
        print("Errado para 'ana'.")
    
    teste_pontual = ["gustavo", "Thiago", "marta", "Ricardo"]
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
    