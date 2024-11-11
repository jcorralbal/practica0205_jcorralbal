#Escribir una función que reciba una muestra de números en una lista y 
#devuelva su media.

import statistics
numero = ""
numeros = []

while numero != "fin":
    numero = input("Introduzca un numero: ")
    numeros.append(numero)
numeros.pop(len(numeros)-1)
numeros = list(map(float, numeros))

def media(n):
    return statistics.mean(n)

resultado =  media(numeros)
print(f"La media de su lista es {resultado}")

"""
Este código tiene una función que calcula la media de una lista de números.
Primero se pidea al usuario que introduzca números para crear la lista
y escribiendo “fin” para terminarcla lista. Los números introducidos se 
guardan en la lista “numeros”

Luego se elimina la palabra “fin” de la lista con numeros.pop(len(numeros)-1),
ya que es el último elemento, y se convierten los elementos de la lista a
números de tipo float usando numeros = list(map(float, numeros)).

La función media(n) utiliza el statistics para calcular la media de
la lista de números, gracias a que hemos introducido al princio¡pio del todo
import statistics. Finalmente se imprime el resultado que es 
la función media sobre la lista numeros.
"""