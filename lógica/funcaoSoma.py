def soma (x, y, z):
    print(x + y + z)
    return x + y + z

def multiplica(x, y, z):
    return x * y * z

def nome_do_seu_time ():
    return "SPFC"

def quieta():
    x = 10 + 20
    print("O valor calculado é", x)

if __name__ == "__main__":
    import sys
    soma(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
else:
    quieta()

#print (soma(10, 20, 50))
#print (soma(-20, 100, 200))

# from nome_modulo import nome_funcao
# Importar apenas uma função específica e não todo o código
