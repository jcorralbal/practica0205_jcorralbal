#Escribir una función que calcule el área de un círculo y otra que calcule el
#volumen de un cilindro usando la primera función.

import math # lo utilizo para poder poner pi

def area_circu(radio):
    area = math.pi * (radio ** 2)
    return area

resultado_area = area_circu(6)
print(f"El área es {resultado_area:.2f}")

def volumen_cilindro(radio_nuevo, altura):
    volumen = area_circu(radio_nuevo) * altura
    return volumen

resultado_volumen = volumen_cilindro(6, 9)
print(f"El volumen de el cilindro es {resultado_volumen:.2f}")


"""
Este código tiene dos funciones
Una para calcular el área de un círculo y otra
para calcular el volumen de un cilindro usando la primera función

la función area_circu(radio)
Calcula el área de un círculo dado su radio utilizando la fórmula
La función utiliza math.pi para obtener un que valor mas 
exacto de π en lugar de poner 3,1416

la función volumen_cilindro(radio_nuevo, altura)
calcula el volumen de un cilindro usando el área de la base y multiplicándola
por la altura del cilindro
utiliza la función anterior para calcular el área

Al final el programa imprime el área del círculo y el volumen del cilindro
"""

    