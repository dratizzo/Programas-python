def computador_escolhe_jogada(pecas_mesa, maximo_retirar):
    print("-Vez do computador.")
    #x -> número de peças que serão removidas
    x = i = produto = 1

    #se nº de peças na mesa menor que máximo_retirar, remove o nº de peças na mesa
    if pecas_mesa <= maximo_retirar:
        x = pecas_mesa
        print("Peças removidas na jogada:", x)
        print("Peças restantes na mesa:", pecas_mesa - x)

    #acha o múltiplo de (m+1) mais próximo do número de peças na mesa
    while produto < pecas_mesa:
        produto = (maximo_retirar + 1) * i
        i += 1
            
    #retira o valor de peças na mesa para chegar no múltiplo mais próximo de (m+1)
    if produto - pecas_mesa <= maximo_retirar:
        print("Peças removidas na jogada:", x)
        print("Peças restantes na mesa:", pecas_mesa - x)
        return produto - pecas_mesa
    else:
        print("Peças removidas na jogada:", x)
        print("Peças restantes na mesa:", pecas_mesa - x)
        return maximo_retirar

def usuario_escolhe_jogada(pecas_mesa, qtd_remover):
    print("-Vez do jogador.")
    testa_nPecas = True
    
    while testa_nPecas:
        x = int(input("Quantas peças quer remover: "))
        if x <= pecas_mesa and x <= qtd_remover:
            testa_nPecas = False
        else:
            print("Informe uma jogada válida...")

    print("Peças removidas na jogada:", x)
    print("Peças restantes na mesa:", pecas_mesa - x)
    
    return x
    
def partida():
    n = int(input("Número inicial de peças: "))
    m = int(input("Máximo de peças possível retirar: "))

    #Se não for múltiplo, o jogador começa 
    if n % (m + 1) == 0:
        print("Você começa!")
        while n != 0:
            n = n - usuario_escolhe_jogada(n, m)
            if n == 0:
                print("Você ganhou!")
            
            else:
                n = n - computador_escolhe_jogada(n, m)
                if n == 0:
                    print("O computador ganhou!")

    #Se n for múltimo de (m+1) o computador começa           
    else:
        print("Computador começa!")
        
        while n != 0:
            n = n - computador_escolhe_jogada(n, m)
            if n == 0:
                print("O computador ganhou!")
            else:
                n = n - usuario_escolhe_jogada(n, m)
                if n == 0:
                    print("Você ganhou!")

#No campeonato ocorrem três partidas em sequência
def campeonato():
    cont = 0
    #while <= 2:
        #partida()
        #cont += 1

def main():
    print("Bem vindo...")


#testar jogada do computador
#checar, simular uma partida, valores pre definidos
#checar campeonato



        
