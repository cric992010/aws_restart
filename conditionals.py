import random # Biblioteca para utilizar números aleatorios


print("\t\tBienvenidos a nuestro juego de adivina el número")
print("\nLa regla es simple: pensaré un número y tú lo adivinas")

number = random.randint(1,10)

#print(number)

isGuessRight = False

while isGuessRight != True:
    # continuo con el juego
    guess = int(input("Adivina un número entre 1 y 10: "))
    # si el número que ingreso es igual al que tengo
    if guess == number:
        print(f"¡Adivinaste! El número es {guess}")
        isGuessRight = True
    elif guess > 10:
        print("No pues cuate, es mayor a 10.")    
    elif guess > number:
        print("JIJIJIJII te pasaste cuate")
    elif guess < number:
        print("El numero es mas grande mi bro")
    else:
        print("ERROR")