#Escribir una función que reciba un número entero positivo y devuelva su 
#factorial. Realiza el ejercicio mediante bucles interactivos y mediante una
#función recursiva.

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = int(input("Introduzca un número entero positivo: "))
print(f"El factoriales : {factorial(numero)}")

"""
Esta función calcula el factorial de un número entero positivo introducido
por el usuario.La función multiplica todos los números desde
1 hasta n (que es la variable que introduce el ususario en forma de input)
y devuelve el resultado. Al final el programa muestra el factorial
calculado con el print.
"""