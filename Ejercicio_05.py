#Escribir una función que reciba una muestra de números en una lista y 
#devuelva otra lista con sus valores al cuadrado.

numeros = []
numero = ""

while numero != "fin":
    numero = input("Introduzca un números para crear una lista: ")
    numeros.append(numero)
numeros.pop(len(numeros)-1)
numeros= list(map(int, numeros))

def lista_al_cuadrado(n):
    nueva_lista = []
    for i in n:
        nuevos_numeros = i ** 2
        nueva_lista.append(nuevos_numeros)
    return nueva_lista

print(lista_al_cuadrado(numeros))

"""
lA función recibe una lista de números y devuelve otra
lista con los valores al cuadrado. Primero se pide al usuario que introduzca
números para crear la lista e introduciendo la oalabra fin para que termine la lista.
Los números introducidos se almacenan en la lista "numeros". 
Luego, se elimina la palabra "fin" con numeros.pop(len(numeros)-1) ya que localiza el 
último elemento de la lista que es fin y lo elimina de la lista y
y por último se convierten los numeros de lista a enteros con list(map(int, numeros))

La función coge la lista de números y crea una nueva
lista donde cada elemento es el cuadrado del número de la lista original. 
esgtos nuevos numeros se introducen en la nueva lista con 
nueva_lista.append(nuevos_numeros) gracia a append
Para terminar se imprime la nueva lista.
"""