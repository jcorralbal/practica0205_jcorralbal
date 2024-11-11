#Escribir una función que reciba un fragmento de texto en una cadena de 
#caracteres y devuelva un diccionario con cada palabra que contiene y su 
#frecuencia. Escribir otra función que reciba el diccionario generado con la
#función anterior y devuelva una tupla con la palabra más repetida y su 
#frecuencia.

def contar_palabras(texto):
    texto = texto.lower()
    palabras = texto.split()
    frecuencias = {}
    for palabra in palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias

def palabra_mas_repetida(frecuencias):
    max_palabra = max(frecuencias, key=frecuencias.get)
    max_frecuencia = frecuencias[max_palabra]
    return (max_palabra, max_frecuencia)

texto = input("Introduzca una frase: ")
frecuencias = contar_palabras(texto)
print("Frecuencias de palabras:")
print(frecuencias)

palabra, frecuencia = palabra_mas_repetida(frecuencias)

print(f"\nLa palabra más repetida es '{palabra}'
       con una frecuencia de {frecuencia}.")

"""
Este código define dos funciones para analizar una frase. La función
contar_palabras(texto) recibe una frase como str y devuelve un diccionario con cada
palabra y su frecuencia. Convierte el texto a minúsculas y lo divide en palabras
para contar cuántas veces aparece cada una.

La función palabra_mas_repetida(frecuencias) toma el diccionario de frecuencias
y devuelve una tupla con la palabra más repetida y su frecuencia. Utiliza la
función max() para encontrar la clave con el valor máximo.

Al final, el programa solicita al usuario una frase, muestra el diccionario de
frecuencias, y luego indica cuál es la palabra más repetida y cuántas veces
aparece.
"""