x = int(input("Número inteiro: "))

if x % 3 == 0 and x % 5 == 0: 
    print("FizzBuzz")

elif x % 3 == 0: #Divisível por 3
    print("Fizz")
    
elif x % 5 == 0: #Divisível por 5
    print("Buzz")
    
else:
    print(x)