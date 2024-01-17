"""
Ejercicio 2: Calculadora de factorial

Escribe un programa que solicite al usuario un número entero no negativo y calcule su factorial. 
El factorial de un número entero positivo 'n' se define como el producto de todos los enteros desde 1 hasta 'n'.
Utiliza un bucle para realizar el cálculo y muestra el resultado. Si el usuario ingresa un número negativo, muestra un mensaje de error y pide un número válido.

Estos ejercicios son sencillos pero pueden ser efectivos para reforzar conceptos de condicionales y bucles en Python. 
Los estudiantes pueden empezar a practicar con estos y luego avanzar a problemas más complejos a medida que ganen confianza en su programación.
"""
import math

enteroNoNegativo = int(input("Ingres un numero entero positivo para saber su factorial: "))

numeroFactorial = enteroNoNegativo

numeroFactorial = math.factorial(enteroNoNegativo)
print(f"El factorial de {enteroNoNegativo} es {numeroFactorial}")


"""
Ejercicio 3: Contador de números pares e impares

Escribe un programa que solicite al usuario un número entero positivo. Luego, utiliza un bucle para contar 
y mostrar la cantidad de números pares e impares en el rango desde 1 hasta el número ingresado por el usuario. Finalmente, muestra los resultados.

Por ejemplo, si el usuario ingresa el número 10, el programa debe mostrar algo como:

mathematica
Copy code
Números pares: 5
Números impares: 5
Este ejercicio te permitirá practicar el uso de bucles, condicionales y contar elementos en un rango.

"""

enteroBucle = int(input("Ingresa un entero positivo para saber los pares e impares: "))
contadorImpares = 0
contadorPares = 0
for x in range(1, enteroBucle + 1):
    if(x % 2 == 0):
        contadorPares += 1
    else:
        contadorImpares+=1

#No poner { } me vuelve loco :v

print("Los impar es son: ", contadorImpares)
print("Los pares son ", contadorPares)



