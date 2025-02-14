'''
Escrever uma função que recebe uma lista de
Strings contendo nomes de pessoas como parâmetro
e devolve o nome mais curto. A função deve ignorar
espaços antes e depois do nome e deve devolver o nome
"capitalizado", i.e., apenas com a 1a letra maiúscula.
'''

lista_de_nomes = ["   ana   ", "josé", "Arquibaldo",
                   "Alouhis"]

def mais_curto(lista_de_nomes):
    nome_mais_curto = lista_de_nomes[0]
    
    for i in range(0, len(lista_de_nomes), 1):
        lista_de_nomes[i] = lista_de_nomes[i].strip()
        
        if (len(lista_de_nomes[i]) < len(nome_mais_curto)):
            nome_mais_curto = lista_de_nomes[i]

    return nome_mais_curto.capitalize()

def testa_mais_curto():
    lista_de_nomes = [" apyr ", "juninho", "    juREGson    "]
    if (mais_curto(lista_de_nomes) == "Apyr"):
        print("Correto para 'Apyr'")
    else:
        print("Falha no teste")
    
    lista_de_nomes = ["piracir", "gugu", " je ", "   se   "]
    if (mais_curto(lista_de_nomes) == "Je"):
        print("Correto para 'Je'")
    else:
        print("Falha no teste")
