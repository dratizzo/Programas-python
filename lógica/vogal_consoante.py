def vogal(letra):
    letra = letra.lower()
    
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return True
    else:
        return False

letra = input("Uma letra: ")

print(vogal(letra))
